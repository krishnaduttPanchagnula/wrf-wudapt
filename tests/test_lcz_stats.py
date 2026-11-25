"""Self-checks for LCZ zonal aggregation. Run: ./run.sh run 'python tests/test_lcz_stats.py'"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from netCDF4 import Dataset

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from lcz_stats import zonal_stats  # noqa: E402

TMP = Path("/tmp/opencode/lcz_stats_test")
TMP.mkdir(parents=True, exist_ok=True)


def make(path: Path, values: np.ndarray, lc: np.ndarray | None = None) -> None:
    with Dataset(path, "w") as ds:
        ds.createDimension("Time", 1)
        ds.createDimension("south_north", 3)
        ds.createDimension("west_east", 3)
        t = ds.createVariable("Times", str, ("Time",))
        t[0] = "2022-07-25T12:00:00"
        if lc is not None:
            v = ds.createVariable("LCZ", "i4", ("Time", "south_north", "west_east"))
            v[0] = lc
        v = ds.createVariable("T2", "f4", ("Time", "south_north", "west_east"))
        v[0] = values


def main() -> None:
    lc = np.array([[1, 1, 2], [1, 2, 2], [2, 2, 2]])
    t2 = np.array([[300, 302, 310], [304, 312, 314], [316, 318, 320]])
    make(TMP / "wrfinput.nc", t2, lc)
    make(TMP / "wrfout.nc", t2)
    df = zonal_stats(TMP / "wrfout.nc", TMP / "wrfinput.nc", variables=("T2",))
    assert set(df["LCZ"]) == {1, 2}, df
    m1 = df.loc[df.LCZ == 1, "T2"].iloc[0]
    m2 = df.loc[df.LCZ == 2, "T2"].iloc[0]
    assert abs(m1 - 302.0) < 1e-5 and abs(m2 - 315.0) < 1e-5, (m1, m2)
    print("LCZ zonal stats self-checks passed:", df[["LCZ", "T2"]].to_dict("records"))


if __name__ == "__main__":
    main()
