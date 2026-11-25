"""Post-process a completed (or partial) case: LCZ zonal stats + validation."""
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from lcz_stats import zonal_stats  # noqa: E402
from validate import load_era5, score, wrf_nearest  # noqa: E402


def main(case: Path) -> None:
    out = ROOT / "output" / case
    tif = ROOT / "data/raw/lcz_europe_4326.tif"
    wrfout = sorted(out.glob("wrfout_d02_*"))[0]
    z = zonal_stats(wrfout, out / "wrfinput_d02", lcz_tif=tif)
    z.to_csv(out / "lcz_zonal_stats.csv", index=False)
    print(f"zonal stats: {len(z)} rows, LCZ classes {sorted(z['LCZ'].unique())}")

    import xarray as xr
    with xr.open_dataset(wrfout) as ds:
        model = wrf_nearest(ds, 45.4937, 9.16646, "T2") - 273.15  # K -> degC
    obs = load_era5(ROOT / "data/raw/era5_milan_2022.json")
    ref = obs["temperature_2m"]
    s = score(model, ref)
    print("T2 vs ERA5 at Milan centre:", s)
    (out / "validation.json").write_text(str(s))


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else Path("case_2022"))
