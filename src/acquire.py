"""Download every no-credential input and record sha256 + retrieval time.

Run inside the container: ./run.sh run 'python src/acquire.py'
FNL 2020 would need a UCAR/GDEX account; this experiment uses AWS GFS 2022.
"""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
SOURCES = yaml.safe_load((ROOT / "config" / "sources.yaml").read_text())

# name -> (url, filename). URLs come from config/sources.yaml.
TARGETS = {
    "lcz_milan": (SOURCES["lcz"]["primary"]["geotiff"], "lcz_milan_oa96.tif"),
    "lcz_ucp_lookup": (SOURCES["lcz"]["properties"]["w2w_lookup"], "LCZ_UCP_lookup.csv"),
    "geog_low_res": (
        SOURCES["static_geography"]["base_url"] + "geog_low_res_mandatory.tar.gz",
        "geog_low_res_mandatory.tar.gz"),
    "geog_lcz": (
        SOURCES["static_geography"]["base_url"] + "cglc_modis_lcz_global.tar.gz",
        "cglc_modis_lcz_global.tar.gz"),
    "lcz_europe": (
        SOURCES["lcz"]["european_map"]["url"], "lcz_europe.tif"),
    "gfs_vtable": (
        "https://raw.githubusercontent.com/wrf-model/WPS/develop/ungrib/Variable_Tables/Vtable.GFS",
        "Vtable.GFS"),
    "validation_era5": (
        SOURCES["meteorology"]["validation_2022"]["open_meteo"]["url"],
        "era5_milan_2022.json"),
}

# WRF initial + lateral boundary conditions: 6-hourly GFS analyses.
TEMPLATE = SOURCES["meteorology"]["selected"]["url_template"]
for day in ("20220724", "20220725", "20220726", "20220727"):
    for hour in ("00", "06", "12", "18"):
        TARGETS[f"gfs_{day}_{hour}"] = (
            TEMPLATE.replace("YYYYMMDD", day).replace("HH", hour),
            f"gfs.t{hour}z.pgrb2.0p25.f000.{day}",
        )


def fetch(url: str, dest: Path) -> dict:
    if dest.exists() and dest.stat().st_size > 0:
        print(f"skip existing {dest.name}")
    else:
        print(f"GET {url} -> {dest.name}", flush=True)
        with requests.get(url, stream=True, timeout=300) as r:
            r.raise_for_status()
            with dest.open("wb") as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
    h = hashlib.sha256()
    with dest.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return {"url": url, "file": dest.name, "bytes": dest.stat().st_size,
            "sha256": h.hexdigest(), "retrieved_utc": datetime.now(timezone.utc).isoformat()}


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    manifest = []
    for name, (url, filename) in TARGETS.items():
        try:
            manifest.append({"name": name, **fetch(url, RAW / filename)})
        except Exception as e:  # a missing source must be visible, not hidden
            print(f"FAILED {name}: {e}", flush=True)
            manifest.append({"name": name, "url": url, "error": str(e)})
    (RAW / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"\n{len(manifest)} entries; {sum('error' not in m for m in manifest)} downloaded")


if __name__ == "__main__":
    main()
