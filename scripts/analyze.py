"""Final analysis of the Milan experiment.

Usage: ./run.sh run 'python scripts/analyze.py [baseline_dir] [counterfactual_dir]'
Writes tables and a short report to output/results/.
"""
import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr
from sklearn.model_selection import GroupKFold

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from compare import compare, load_zonal  # noqa: E402
from emulator import Emulator, blocked_score  # noqa: E402
from lcz_stats import sample_lcz, wrf_times, zonal_stats  # noqa: E402
from validate import load_era5, score, wrf_nearest  # noqa: E402

BASE = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "output/case_2022"
CF = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "output/case_2022_lu80"
OUT = ROOT / "output/results"
TIF = ROOT / "data/raw/lcz_europe_4326.tif"
ERA5 = ROOT / "data/raw/era5_milan_2022.json"
LAT, LON = 45.4937, 9.16646
SPINUP_H = int(os.environ.get("SPINUP_H", 6))
OUT.mkdir(parents=True, exist_ok=True)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def zonal(case: Path, name: str, lcz: np.ndarray):
    wrfout = sorted(case.glob("wrfout_d02_*"))[-1]
    df = zonal_stats(wrfout, case / "wrfinput_d02", domain=2, lcz=lcz)
    df["hour"] = df["time"].dt.hour
    df = df[df["hour"] >= SPINUP_H].copy()
    with xr.open_dataset(case / "wrfinput_d02") as ds:
        static = pd.DataFrame({
            "LCZ": lcz.ravel(),
            "URB_FRAC": ds["LANDUSEF"].isel(Time=0).values[12].ravel(),
            "FRC_URB2D": ds["FRC_URB2D"].isel(Time=0).values.ravel(),
        })
    by_lcz = static[static.LCZ > 0].groupby("LCZ").mean()
    df["URB_FRAC"] = df.LCZ.map(by_lcz.URB_FRAC)
    df["FRC_URB2D"] = df.LCZ.map(by_lcz.FRC_URB2D)
    df["case"] = name
    df.to_csv(OUT / f"zonal_{name}.csv", index=False)
    return df


def verify(case: Path) -> dict:
    from netCDF4 import Dataset
    p = sorted(case.glob("wrfout_d02_*"))[-1]
    with Dataset(p) as ds:
        raw = ds["Times"][:]
        names = ["".join(c.astype(str)).strip() for c in raw.reshape(raw.shape[0], -1)]
        t = pd.to_datetime([s.replace("_", " ") for s in names], utc=True)
        t2, lat, lon = ds["T2"][:], ds["XLAT"][:], ds["XLONG"][:]
        fmt = ds.data_model
    return {"file": str(p), "format": fmt, "frames": len(t),
            "first": str(t[0]), "last": str(t[-1]),
            "finite_T2": bool(np.isfinite(t2).all()),
            "lat_range": [float(lat.min()), float(lat.max())],
            "lon_range": [float(lon.min()), float(lon.max())]}


def report(results: dict) -> None:
    v, val = results["verification"], results["validation"]
    lines = [
        "# Milan WRF-WUDAPT experiment — results", "",
        "25 Jul 2022, 00–18 UTC (6 h spin-up, 12 h analysis); 9 km / 3 km nested.",
        "LCZ drives urban extent through `w2w`; per-LCZ urban canopy parameters are",
        "not ingested by this WRF build (documented shortcut in README.md).", "",
        "## NetCDF verification", "",
        f"- Baseline: `{v['baseline']['file']}` — {v['baseline']['format']}, "
        f"{v['baseline']['frames']} frames, {v['baseline']['first']} → {v['baseline']['last']}, "
        f"finite T2: {v['baseline']['finite_T2']}.",
    ]
    if "lu80" in v:
        lines.append(f"- Counterfactual: `{v['lu80']['file']}` — {v['lu80']['format']}, "
                     f"{v['lu80']['frames']} frames, finite T2: {v['lu80']['finite_T2']}.")
    lines += ["", "## Independent validation (ERA5 point series, reanalysis — not station data)", "",
              "| window | n | bias (K) | MAE (K) | RMSE (K) |",
              "|---|---:|---:|---:|---:|"]
    for name, s in [("full 00–18Z", val["full"]), ("held-out 12–18Z", val.get("held_out_12_18Z"))]:
        if s:
            lines.append(f"| {name} | {s['n']} | {s['bias']:.3f} | {s['mae']:.3f} | {s['rmse']:.3f} |")
    if "counterfactual" in results:
        c = results["counterfactual"]
        lines += ["", "## Causal comparison (counterfactual WRF run)", "",
                  f"Intervention: {c['intervention']}. n={c['n_built']} LCZ×hour pairs in built classes.",
                  f"Mean ΔT2 (LCZ 1–10) = {c['mean_delta_T2_K_built']:+.3f} K.",
                  "", "| LCZ | mean ΔT2 (K) | n |", "|---:|---:|---:|"]
        for r in c["by_lcz"]:
            if r["LCZ"] <= 10:
                lines.append(f"| {r['LCZ']:.0f} | {r['mean']:+.3f} | {int(r['count'])} |")
        e = results["emulator"]
        lines += ["", "## Emulator (trained on baseline + counterfactual WRF runs)", "",
                  f"Features: {', '.join(e['features'])}; monotonic constraints: {e['monotonic_cst']}.",
                  "| validation | RMSE (K) | MAE (K) | R² | naive RMSE (K) |",
                  "|---|---:|---:|---:|---:|"]
        for name in ("lcZ_blocked", "time_blocked_2h"):
            s = e[name]
            if s:
                lines.append(f"| {name} | {s['rmse']:.3f} | {s['mae']:.3f} | {s['r2']:.3f} | "
                             f"{s['naive_rmse']:.3f} |")
        lo, hi = e["prediction_interval_90pct_K"]
        cooling = sum(1 for r in c["by_lcz"] if r["LCZ"] <= 10 and r["mean"] < 0)
        total = sum(1 for r in c["by_lcz"] if r["LCZ"] <= 10)
        lines += ["", f"90% residual interval: [{lo:+.3f}, {hi:+.3f}] K.",
                  f"Support check: {e['support_check']}.", "",
                  f"LCZ-blocked R² = {e['lcZ_blocked']['r2']:.3f} (vs climatology): "
                  "no transferable skill across LCZ; time-blocked skill mostly tracks the diurnal cycle.",
                  "The temperature response above comes from the perturbed-physics WRF run,",
                  "not from perturbing a regression input.",
                  f"Response is mixed across built LCZs ({cooling} of {total} cool); "
                  "no uniform city-wide cooling is claimed."]
    lines += ["", "## Limitations", "",
              "- ERA5 is a reanalysis, not station observations; it shares no GFS ancestry.",
              "- Only one counterfactual (80% urban land use replaced) and an 18 h window; "
              "the emulator has two urban-fraction levels.",
              "- Urban morphology is WRF default; LCZ only sets urban extent (README shortcut).", ""]
    (OUT / "REPORT.md").write_text("\n".join(lines))


def blocked_residuals(df, emu, group_col):
    res = []
    n_splits = min(5, df[group_col].nunique())
    for train, test in GroupKFold(n_splits=n_splits).split(df, groups=df[group_col]):
        m = emu.__class__(emu.features, emu.target, emu.monotone).fit(df.iloc[train])
        res.extend(df.iloc[test][emu.target].to_numpy() - m.model.predict(df.iloc[test][emu.features]))
    return np.asarray(res)


def main() -> None:
    lcz = sample_lcz(BASE / "wrfinput_d02", TIF)
    np.save(OUT / "lcz_grid.npy", lcz)

    a = zonal(BASE, "baseline", lcz)
    results = {"cases": {"baseline": str(BASE)}}

    # Independent point validation (ERA5, not station data): full window + held-out tail.
    with xr.open_dataset(sorted(BASE.glob("wrfout_d02_*"))[-1]) as ds:
        model = wrf_nearest(ds, LAT, LON, "T2")
    obs = load_era5(ERA5)["temperature_2m"] + 273.15
    held = model.index >= pd.Timestamp("2022-07-25T12:00Z")
    results["validation"] = {
        "source": "ERA5 via Open-Meteo (reanalysis, not station observations)",
        "full": score(model, obs),
        "held_out_12_18Z": score(model[held], obs) if held.any() else None,
    }

    b = None
    if CF.exists() and list(CF.glob("wrfout_d02_*")):
        b = zonal(CF, "lu80", lcz)
        results["cases"]["lu80"] = str(CF)
        m = compare(a, b, "T2")
        m.to_csv(OUT / "compare_lu80.csv", index=False)
        cf_summary = m.groupby("LCZ")["delta_T2"].agg(["mean", "count"]).reset_index()
        cf_summary.to_csv(OUT / "counterfactual_by_lcz.csv", index=False)
        built = m[m["LCZ"] <= 10]
        results["counterfactual"] = {
            "intervention": "80% of urban land-use fraction replaced by grassland in LCZ 1-10, re-run WRF",
            "mean_delta_T2_K_built": float(built["delta_T2"].mean()),
            "n_built": int(len(built)),
            "by_lcz": cf_summary.to_dict("records"),
        }

        # Emulator trained only on the counterfactual ensemble (two WRF runs).
        train = pd.concat([a, b], ignore_index=True)
        feats = ["hour", "LCZ", "URB_FRAC", "FRC_URB2D"]
        mono = {"hour": 0, "LCZ": 0, "URB_FRAC": -1, "FRC_URB2D": 1}
        train["time_block"] = train["hour"] // 2
        emu = Emulator(feats, "T2", mono).fit(train)
        res = blocked_residuals(train, emu, "LCZ")
        results["emulator"] = {
            "features": feats,
            "monotonic_cst": mono,
            "random_seed": 42,
            "lcZ_blocked": blocked_score(train, emu, "LCZ"),
            "time_blocked_2h": (blocked_score(train, emu, "time_block")
                                if train["time_block"].nunique() > 1 else None),
            "prediction_interval_90pct_K": [float(np.quantile(res, .05)), float(np.quantile(res, .95))],
            "train_support": emu.train_range,
        }
        try:
            bad = train.iloc[:1][feats].copy()
            bad["URB_FRAC"] = train["URB_FRAC"].min() - 0.1
            emu.predict(bad)
            results["emulator"]["support_check"] = "FAILED (extrapolation accepted)"
        except ValueError:
            results["emulator"]["support_check"] = "passed (out-of-support urban fraction rejected)"

    results["verification"] = {"baseline": verify(BASE)}
    if "lu80" in results["cases"]:
        results["verification"]["lu80"] = verify(CF)
    results["provenance"] = {
        "namelist_sha256": sha256(ROOT / "config/namelist.input"),
        "lcz_tif_sha256": sha256(TIF),
        "era5_retrieved": ERA5.stat().st_mtime,
        "sources": "config/sources.yaml",
    }
    report(results)
    (OUT / "results.json").write_text(json.dumps(results, indent=2, default=str))
    print(json.dumps(results, indent=2, default=str)[:4000])


if __name__ == "__main__":
    main()
