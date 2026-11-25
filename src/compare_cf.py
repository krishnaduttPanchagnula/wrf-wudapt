"""Difference baseline vs counterfactual WRF runs by LCZ."""
import sys
from pathlib import Path

import numpy as np
import xarray as xr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from lcz_stats import zonal_stats  # noqa: E402


def load(case: str) -> Path:
    return sorted((ROOT / "output" / case).glob("wrfout_d02_*"))[0]


def main() -> None:
    tif = ROOT / "data/raw/lcz_europe_4326.tif"
    cases = tuple(sys.argv[1:3]) if len(sys.argv) >= 3 else ("case_2022", "case_2022_soil20")
    z = []
    for c in cases:
        out = ROOT / "output" / c
        d = zonal_stats(load(c), out / "wrfinput_d02", variables=("T2",), lcz_tif=tif)
        z.append(d.rename(columns={"T2": f"T2_{c}"}))
    m = z[0].merge(z[1], on=["time", "LCZ"])
    m["delta_T2_K"] = m[f"T2_{cases[1]}"] - m[f"T2_{cases[0]}"]
    summary = m.groupby("LCZ")["delta_T2_K"].mean().round(3)
    m.to_csv(ROOT / "output/counterfactual_compare.csv", index=False)
    print(summary.to_string())
    print("mean delta (K):", round(float(np.nanmean(summary)), 3))


if __name__ == "__main__":
    main()
