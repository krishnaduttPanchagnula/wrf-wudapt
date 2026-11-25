"""Headless weather digital-twin engine.

A request (lat, lon, radius, date/time) is turned into a WRF case; a proposal
(circular area + land-use change) is turned into a counterfactual WRF run. The
QGIS plugin is a thin front-end over these functions -- no physics lives there.
"""
import json
import math
import os
import re
import shutil
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr

# In a checkout, the project root is the parent of this package. When installed
# with pip, point WRF_TWIN_ROOT at the checkout that contains WRF/WPS and data/.
ROOT = Path(os.environ.get("WRF_TWIN_ROOT", Path(__file__).resolve().parents[1]))
WPS = ROOT / "src/WPS"
WRF = ROOT / "src/WRF"
RAW = ROOT / "data/raw"
GEOG = RAW / "geog/WPS_GEOG_LOW_RES"
URL = ("https://noaa-gfs-bdp-pds.s3.amazonaws.com/gfs.{day}/{hour}/atmos/"
       "gfs.t{hour}z.pgrb2.0p25.f000")
OUTER_DX = 9000
INNER_DX = 3000


@dataclass
class CaseRequest:
    lat: float
    lon: float
    radius_km: float
    start: str                      # ISO, e.g. 2022-07-25T00:00:00Z
    hours: int = 18
    lcz_tif: str | None = None      # only used when the map covers the domain

    def __post_init__(self):
        # WPS interval_seconds = 21600: the window must be a whole number of GFS analyses.
        if self.hours < 6 or self.hours % 6:
            raise ValueError("hours must be >= 6 and a multiple of 6 (GFS is 6-hourly)")

    @property
    def end(self) -> datetime:
        return self.start_dt + timedelta(hours=self.hours)

    @property
    def start_dt(self) -> datetime:
        return pd.to_datetime(self.start, utc=True).to_pydatetime()

    @property
    def grid_n(self) -> int:
        # n = 6k+1 keeps the nested domain centred on the parent grid.
        return 6 * max(5, math.ceil(self.radius_km / 9)) + 1


def _substitute(text: str, pairs: dict) -> str:
    for pattern, replacement in pairs.items():
        text = re.sub(pattern, replacement, text)
    return text


def build_namelists(request: CaseRequest, case: Path) -> None:
    """Write case-specific WPS/WRF namelists from the corrected templates."""
    n = request.grid_n
    parent_start = (n + 1) // 2 - (n - 1) // 6
    s, e = request.start_dt, request.end
    wps = _substitute((ROOT / "config/namelist.wps").read_text(), {
        r"start_date\s*=.*": f"start_date = '{s:%Y-%m-%d_%H:%M:%S}', '{s:%Y-%m-%d_%H:%M:%S}',",
        r"end_date\s*=.*": f"end_date   = '{e:%Y-%m-%d_%H:%M:%S}', '{e:%Y-%m-%d_%H:%M:%S}',",
        r"e_we\s*=.*": f"e_we = {n}, {n},",
        r"e_sn\s*=.*": f"e_sn = {n}, {n},",
        r"i_parent_start\s*=.*": f"i_parent_start = 1, {parent_start},",
        r"j_parent_start\s*=.*": f"j_parent_start = 1, {parent_start},",
        r"ref_lat\s*=.*": f"ref_lat = {request.lat:.6f},",
        r"ref_lon\s*=.*": f"ref_lon = {request.lon:.6f},",
        r"stand_lon\s*=.*": f"stand_lon = {request.lon:.6f},",
        r"geog_data_path\s*=.*": f"geog_data_path = '{GEOG}',",
    })
    wps = wps.replace("PATH_TO_WPS_GEOG", str(GEOG))
    (case / "namelist.wps").write_text(wps)

    wrf = _substitute((ROOT / "config/namelist.input").read_text(), {
        r"start_year\s*=.*": f"start_year = {s.year}, {s.year},",
        r"start_month\s*=.*": f"start_month = {s.month}, {s.month},",
        r"start_day\s*=.*": f"start_day = {s.day}, {s.day},",
        r"start_hour\s*=.*": f"start_hour = {s.hour}, {s.hour},",
        r"end_year\s*=.*": f"end_year = {e.year}, {e.year},",
        r"end_month\s*=.*": f"end_month = {e.month}, {e.month},",
        r"end_day\s*=.*": f"end_day = {e.day}, {e.day},",
        r"end_hour\s*=.*": f"end_hour = {e.hour}, {e.hour},",
        r"e_we\s*=.*": f"e_we = {n}, {n},",
        r"e_sn\s*=.*": f"e_sn = {n}, {n},",
        r"i_parent_start\s*=.*": f"i_parent_start = 1, {parent_start},",
        r"j_parent_start\s*=.*": f"j_parent_start = 1, {parent_start},",
    })
    (case / "namelist.input").write_text(wrf)


def fetch_gfs(request: CaseRequest) -> list[Path]:
    """Download the 6-hourly GFS f000 analyses covering the requested window."""
    import requests
    files = []
    t = request.start_dt.replace(minute=0, second=0, microsecond=0)
    # round down to the previous 6-hourly analysis, include one before start
    t -= timedelta(hours=t.hour % 6 + 6)
    while t <= request.end:
        day, hour = f"{t:%Y%m%d}", f"{t:%H}"
        dest = RAW / f"gfs.t{hour}z.pgrb2.0p25.f000.{day}"
        if not dest.exists() or dest.stat().st_size < 1_000_000:
            url = URL.format(day=day, hour=hour)
            print(f"GET {url}", flush=True)
            with requests.get(url, stream=True, timeout=900) as r:
                r.raise_for_status()
                with dest.open("wb") as f:
                    for chunk in r.iter_content(1 << 20):
                        f.write(chunk)
        files.append(dest)
        t += timedelta(hours=6)
    return files


def _run(cmd, cwd, log) -> None:
    with open(log, "a") as out:
        subprocess.run(cmd, cwd=cwd, stdout=out, stderr=subprocess.STDOUT, check=True)


def prepare_case(request: CaseRequest, case: Path) -> Path:
    """Run WPS + real.exe for a request. Result: case dir with wrfinput/wrfbdy."""
    case.mkdir(parents=True, exist_ok=True)
    (case / "request.json").write_text(json.dumps(asdict(request), indent=2))
    (case / "prepare.log").write_text("")
    if not GEOG.exists():
        raise FileNotFoundError(f"geography not extracted: {GEOG}")
    build_namelists(request, case)
    files = fetch_gfs(request)

    for f in WPS.glob("GRIBFILE.AA*"):
        f.unlink()
    for f in WPS.glob("FILE:*"):
        f.unlink()
    for i, src in enumerate(files):
        letter = chr(ord("A") + i // 26) + chr(ord("A") + i % 26)
        (WPS / f"GRIBFILE.A{letter}").symlink_to(src)
    vtable = RAW / "Vtable.GFS"
    if vtable.exists():
        shutil.copy(vtable, WPS / "Vtable")
    (WPS / "namelist.wps").unlink(missing_ok=True)
    (WPS / "namelist.wps").symlink_to(case / "namelist.wps")
    _run(["./geogrid.exe"], WPS, case / "geogrid.log")
    for src in WPS.glob("geo_em.d0*.nc"):
        shutil.copy(src, case / src.name)

    (case / "w2w").mkdir(exist_ok=True)
    if request.lcz_tif and Path(request.lcz_tif).exists():
        import rasterio
        with rasterio.open(request.lcz_tif) as r:
            covers = r.bounds.left <= request.lon <= r.bounds.right and \
                     r.bounds.bottom <= request.lat <= r.bounds.top
        if covers:
            for src in case.glob("geo_em.d0*.nc"):
                shutil.copy(src, case / "w2w" / src.name)
            shutil.copy(request.lcz_tif, case / "w2w/lcz.tif")
            _run(["w2w", ".", "lcz.tif", "geo_em.d02.nc", "-l", "0",
                  "--lcz-ucp", str(RAW / "LCZ_UCP_lookup.csv")],
                 case / "w2w", case / "w2w.log")
            shutil.copy(case / "w2w/geo_em.d02_LCZ_extent.nc", WPS / "geo_em.d02.nc")

    _run(["./ungrib.exe"], WPS, case / "ungrib.log")
    _run(["./metgrid.exe"], WPS, case / "metgrid.log")

    from netCDF4 import Dataset
    met = sorted(WPS.glob("met_em.d01.*.nc"))[0]
    with Dataset(met) as ds:
        levels = ds.dimensions["num_metgrid_levels"].size
    inp = (case / "namelist.input").read_text().replace(
        "num_metgrid_levels = 34", f"num_metgrid_levels = {levels}")
    (case / "namelist.input").write_text(inp)

    (WRF / "run/namelist.input").unlink(missing_ok=True)
    (WRF / "run/namelist.input").symlink_to(case / "namelist.input")
    for f in WRF.glob("run/met_em.d0*.nc"):
        f.unlink()
    for f in WPS.glob("met_em.d0*.nc"):
        (WRF / "run" / f.name).symlink_to(f)
    _run(["./real.exe"], WRF / "run", case / "real.log")
    if "SUCCESS COMPLETE REAL_EM INIT" not in (case / "real.log").read_text(errors="replace"):
        raise RuntimeError(f"real.exe failed; see {case / 'real.log'}")
    for name in ("wrfinput_d01", "wrfinput_d02", "wrfbdy_d01"):
        shutil.copy(WRF / "run" / name, case / name)
    print(f"prepared {case}")
    return case


def run_baseline(case: Path) -> Path:
    """Run foreground WRF for a prepared case; outputs stay in ``case``."""
    case = case.resolve()
    (WRF / "run/namelist.input").unlink(missing_ok=True)
    (WRF / "run/namelist.input").symlink_to(case / "namelist.input")
    for f in (WRF / "run").glob("wrfout_d0*"):
        f.unlink()
    _run(["./wrf.exe"], WRF / "run", case / "wrf.log")
    if "SUCCESS COMPLETE WRF" not in (case / "wrf.log").read_text(errors="replace"):
        raise RuntimeError(f"wrf.exe failed; see {case / 'wrf.log'}")
    for f in (WRF / "run").glob("wrfout_d0*"):
        shutil.copy(f, case / f.name)
    print(f"baseline done -> {case}")
    return case


def apply_scenario(case: Path, scenario: dict, out: Path) -> Path:
    """Perturb land use in a circular area and run WRF from that state."""
    area = scenario["area"]
    from_cat, to_cat = scenario.get("from_cat", 13), scenario.get("to_cat", 10)
    fraction = float(scenario.get("fraction", 0.8))
    out.mkdir(parents=True, exist_ok=True)
    for f in ("namelist.input", "wrfinput_d01", "wrfbdy_d01"):
        shutil.copy(case / f, out / f)
    with xr.open_dataset(case / "wrfinput_d02") as ds:
        modified = ds.copy(deep=True)
        lat = modified["XLAT"].isel(Time=0).values
        lon = modified["XLONG"].isel(Time=0).values
        r = 6371.0
        p1, p2 = np.radians(area["lat"]), np.radians(lat)
        dphi = p2 - p1
        dl = np.radians(lon - area["lon"])
        a = np.sin(dphi / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2
        mask = 2 * r * np.arcsin(np.sqrt(a)) <= area["radius_km"]
        lu = modified["LANDUSEF"].values
        src, dst = lu[:, from_cat - 1], lu[:, to_cat - 1]
        moved = np.minimum(src[:, mask], fraction * src[:, mask])
        src[:, mask] -= moved
        dst[:, mask] += moved
        idx = modified["LU_INDEX"].values
        idx[:, mask] = lu[:, :, mask].argmax(axis=1) + 1
        modified.to_netcdf(out / "wrfinput_d02")
    return _run_perturbed(case, out, scenario)


def _run_perturbed(case: Path, out: Path, scenario: dict) -> Path:
    """Link the shared WRF inputs into a perturbed case and run it."""
    for f in case.glob("met_em.d0*.nc"):
        (out / f.name).symlink_to(f.resolve())
    for f in (WRF / "run").iterdir():
        if f.is_file() and f.name not in {
                "namelist.input", "wrfinput_d01", "wrfinput_d02", "wrfbdy_d01"} and \
                not f.name.startswith("wrfout") and not f.name.startswith("rsl.") and \
                not (out / f.name).exists():
            (out / f.name).symlink_to(f)
    (out / "scenario.json").write_text(json.dumps(scenario, indent=2))
    with open(out / "wrf.log", "w") as log:
        subprocess.run([str(WRF / "main/wrf.exe")], cwd=out,
                       stdout=log, stderr=subprocess.STDOUT, check=True)
    if "SUCCESS COMPLETE WRF" not in (out / "wrf.log").read_text(errors="replace"):
        raise RuntimeError(f"scenario wrf.exe failed; see {out / 'wrf.log'}")
    print(f"scenario done -> {out}")
    return out


def warm_case(case: Path, out: Path, delta_t_k: float) -> Path:
    """Copy a prepared case and add a uniform temperature offset to initial/boundary fields.

    This is a pseudo-global-warming (PGW) perturbation: WRF physics still runs
    the scenario, so no regression is asked to extrapolate. The offset and its
    provenance must be supplied by the caller; no CMIP6 data is bundled.
    """
    from netCDF4 import Dataset

    delta = float(delta_t_k)
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    shutil.copy(case / "namelist.input", out / "namelist.input")
    for name in ("wrfinput_d01", "wrfinput_d02", "wrfbdy_d01"):
        shutil.copy(case / name, out / name)
        with Dataset(out / name, "a") as ds:
            variables = [v for v in ds.variables if v == "T" or v.startswith("T_B")]
            if not variables:
                raise RuntimeError(f"no temperature field in {name}; cannot verify warming")
            first = ds.variables[variables[0]]
            before = float(np.mean(first[:]))
            for var in variables:
                ds.variables[var][:] = np.asarray(ds.variables[var][:]) + delta
            after = float(np.mean(first[:]))
            if not np.isclose(after - before, delta, atol=1e-3):
                raise RuntimeError(f"warming did not bite in {name}")
    return out


def apply_future_climate(case: Path, scenario: dict, out: Path) -> Path:
    """Run WRF with a supplied AR6/SSP temperature offset (PGW-style)."""
    warm_case(case, out, scenario["delta_T_K"])
    return _run_perturbed(case, out, scenario)


def write_comparison_report(results: Path, out: Path | None = None) -> Path:
    """Write the hourly base / proposal / difference page next to a study's CSVs."""
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    from compare import (export_delta_geotiff, load_zonal, side_by_side,
                         side_by_side_html)

    results = Path(results)
    out = Path(out) if out else results
    out.mkdir(parents=True, exist_ok=True)
    a = load_zonal(results / "zonal_baseline.csv")
    b = load_zonal(results / "zonal_scenario.csv")
    metrics = results / "results.json"
    validation = json.loads(metrics.read_text()).get("validation") if metrics.exists() else None
    path = out / "base_proposal_difference.html"
    path.write_text(side_by_side_html(side_by_side(a, b), validation))
    points = results / "delta_t2_points.csv"
    if points.exists():
        export_delta_geotiff(pd.read_csv(points), out / "delta_t2.tif")
    write_validation_report(results, out)
    return path


def write_validation_report(results: Path, out: Path | None = None) -> Path:
    """Compile the validation, skill and provenance in results.json into a document."""
    results = Path(results)
    out = Path(out) if out else results
    out.mkdir(parents=True, exist_ok=True)
    path = out / "VALIDATION.md"
    metrics = results / "results.json"
    data = json.loads(metrics.read_text()) if metrics.exists() else {}
    validation = data.get("validation")

    def num(value, digits=3):
        return f"{value:.{digits}f}" if isinstance(value, (int, float)) else "—"

    lines = [f"# Validation — generated from `{metrics}`", ""]
    if not validation:
        lines += [f"No validation metrics found in `{metrics}`.",
                  "Do not present these results as validated (see CONSTRAINTS.md)."]
    else:
        lines += [f"Source: {validation.get('source', 'unrecorded')}.",
                  "An independent reanalysis is not a station observation; keep the held-out window.",
                  "", "| Window | n | Bias (K) | MAE (K) | RMSE (K) |",
                  "|---|---:|---:|---:|---:|"]
        for label, key in (("Full", "full"), ("Held out 12–18Z", "held_out_12_18Z")):
            s = validation.get(key, {})
            lines.append(f"| {label} | {s.get('n', '—')} | {num(s.get('bias'))} | "
                         f"{num(s.get('mae'))} | {num(s.get('rmse'))} |")
        emulator = data.get("emulator")
        if emulator:
            lines += ["", "## Emulator skill", "",
                      "| Split | RMSE (K) | MAE (K) | R² | Naive RMSE (K) |",
                      "|---|---:|---:|---:|---:|"]
            for label, key in (("LCZ-blocked", "lcZ_blocked"),
                               ("Time-blocked 2h", "time_blocked_2h")):
                s = emulator.get(key, {})
                lines.append(f"| {label} | {num(s.get('rmse'))} | {num(s.get('mae'))} | "
                             f"{num(s.get('r2'))} | {num(s.get('naive_rmse'))} |")
            lines += ["", f"Support check: {emulator.get('support_check', 'not recorded')}."]
        provenance = data.get("provenance")
        if provenance:
            lines += ["", "## Provenance", "",
                      f"- Sources: {provenance.get('sources', 'not recorded')}",
                      f"- Namelist SHA-256: {provenance.get('namelist_sha256', 'not recorded')}",
                      f"- LCZ GeoTIFF SHA-256: {provenance.get('lcz_tif_sha256', 'not recorded')}"]
    path.write_text("\n".join(lines) + "\n")
    return path


def compare_cases(baseline: Path, scenario: Path, out: Path) -> Path:
    """Write tables and QGIS-ready exports: per-cell ΔT2 and zonal means."""
    out.mkdir(parents=True, exist_ok=True)
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    from compare import compare
    from lcz_stats import zonal_stats

    a = sorted(baseline.glob("wrfout_d02_*"))[-1]
    b = sorted(scenario.glob("wrfout_d02_*"))[-1]
    with xr.open_dataset(baseline / "wrfinput_d02") as st:
        lcz = st["LU_INDEX"].isel(Time=0).values
    za = zonal_stats(a, baseline / "wrfinput_d02", lcz=lcz)
    zb = zonal_stats(b, baseline / "wrfinput_d02", lcz=lcz)
    za.to_csv(out / "zonal_baseline.csv", index=False)
    zb.to_csv(out / "zonal_scenario.csv", index=False)
    delta = compare(za, zb, "T2")
    delta.to_csv(out / "delta_by_landuse.csv", index=False)

    with xr.open_dataset(a) as da, xr.open_dataset(b) as db:
        lat = da["XLAT"].isel(Time=0).values
        lon = da["XLONG"].isel(Time=0).values
        d = (db["T2"] - da["T2"]).mean("Time").values
    points = pd.DataFrame({"lat": lat.ravel(), "lon": lon.ravel(),
                           "delta_T2_K": d.ravel()})
    points.to_csv(out / "delta_t2_points.csv", index=False)
    (out / "summary.json").write_text(json.dumps({
        "baseline": str(baseline), "scenario": str(scenario),
        "mean_delta_T2_K": float(np.nanmean(d)),
        "cells_cooled": int(np.nansum(d < 0)), "cells": int(d.size),
    }, indent=2))
    write_comparison_report(out)
    print(f"comparison exported -> {out}")
    return out


def study_name(request: CaseRequest) -> str:
    """Directory name for one study, reused by the CLI and the desktop app."""
    return f"twin_{request.lat:.4f}_{request.lon:.4f}_{request.start_dt:%Y%m%dT%H}"


def run_study(request: CaseRequest, proposal: dict, root: Path) -> Path:
    """Prepare, run, and compare one baseline/counterfactual study."""
    study = Path(root) / study_name(request)
    base = prepare_case(request, study / "baseline")
    run_baseline(base)
    cf = apply_scenario(base, proposal, study / "scenario")
    compare_cases(base, cf, study / "results")
    return study


def compare_years(first: Path, second: Path, out: Path) -> Path:
    """Compare two completed studies by LCZ and calendar hour.

    ``first`` and ``second`` are their ``results/`` directories. Baseline T2 is
    compared directly; when both studies have a counterfactual, their *effects*
    (scenario - baseline) are compared instead, so a change in cooling is not
    mistaken for a change in weather. Years are aligned on month-day and hour.
    """
    import sys
    sys.path.insert(0, str(ROOT / "src"))
    from compare import compare, load_zonal

    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)

    def zonal(results: Path, name: str):
        path = results / f"zonal_{name}.csv"
        return load_zonal(path) if path.exists() else None

    a_base, b_base = zonal(first, "baseline"), zonal(second, "baseline")
    if a_base is None or b_base is None:
        raise FileNotFoundError("both studies need results/zonal_baseline.csv")
    baseline = compare(a_base, b_base, "T2").rename(columns={
        "T2_a": "first_K", "T2_b": "second_K", "delta_T2": "second_minus_first_K"})
    baseline.to_csv(out / "baseline_year_on_year.csv", index=False)

    a_scen, b_scen = zonal(first, "scenario"), zonal(second, "scenario")
    effects = None
    if a_scen is not None and b_scen is not None:
        def effect(base, scen):
            return compare(base, scen, "T2")[["LCZ", "date", "hour", "delta_T2"]]
        effects = effect(a_base, a_scen).merge(
            effect(b_base, b_scen), on=["LCZ", "date", "hour"],
            suffixes=("_first", "_second"))
        effects["second_minus_first_K"] = (
            effects["delta_T2_second"] - effects["delta_T2_first"])
        effects = effects.rename(columns={"delta_T2_first": "first_effect_K",
                                          "delta_T2_second": "second_effect_K"})
        effects.to_csv(out / "effect_year_on_year.csv", index=False)

    def mean(df, column):
        return float(df[column].mean()) if len(df) else None

    def start(results: Path):
        request = results.parent / "baseline" / "request.json"
        return json.loads(request.read_text()).get("start") if request.exists() else None

    summary = {
        "first": str(first), "second": str(second),
        "first_start": start(first), "second_start": start(second),
        "baseline_mean_delta_K": mean(baseline, "second_minus_first_K"),
        "baseline_pairs": int(len(baseline)),
    }
    if effects is not None:
        summary.update({
            "effect_first_mean_K": mean(effects, "first_effect_K"),
            "effect_second_mean_K": mean(effects, "second_effect_K"),
            "effect_change_mean_K": mean(effects, "second_minus_first_K"),
            "effect_pairs": int(len(effects)),
        })
    (out / "years.json").write_text(json.dumps(summary, indent=2))
    print(f"year comparison exported -> {out}")
    return out
