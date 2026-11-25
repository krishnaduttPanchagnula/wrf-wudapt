"""Self-checks for counterfactual generation."""
import sys
from pathlib import Path

import numpy as np
from netCDF4 import Dataset

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from scenarios import perturb_lai, perturb_landuse  # noqa: E402

TMP = Path("/tmp/opencode/scenario_test")
TMP.mkdir(parents=True, exist_ok=True)
SRC, OUT = TMP / "wrfinput.nc", TMP / "wrfinput_lai.nc"
with Dataset(SRC, "w") as ds:
    ds.createDimension("Time", 1)
    ds.createDimension("south_north", 2)
    ds.createDimension("west_east", 2)
    lai = ds.createVariable("LAI", "f4", ("Time", "south_north", "west_east"))
    lai[0] = [[2.0, 2.0], [2.0, 2.0]]
    lc = ds.createVariable("LCZ", "i4", ("Time", "south_north", "west_east"))
    lc[0] = [[1, 2], [1, 2]]


def main() -> None:
    perturb_lai(SRC, OUT, 1.2, lcz_classes=(1,))
    with Dataset(OUT) as ds:
        v = ds["LAI"][0]
        assert np.allclose(v[:, 0], 2.4) and np.allclose(v[:, 1], 2.0), v
    src2, out2 = TMP / "wrfinput_lu.nc", TMP / "wrfinput_lu80.nc"
    with Dataset(src2, "w") as ds:
        ds.createDimension("Time", 1)
        ds.createDimension("land_cat_stag", 21)
        ds.createDimension("south_north", 2)
        ds.createDimension("west_east", 2)
        lu = ds.createVariable("LANDUSEF", "f4",
                               ("Time", "land_cat_stag", "south_north", "west_east"))
        lu[0] = 0.0
        lu[0, 12] = 0.5
        lu[0, 9] = 0.5
        idx = ds.createVariable("LU_INDEX", "f4", ("Time", "south_north", "west_east"))
        idx[0] = 13
    lcz2 = np.array([[1, 2], [1, 2]])
    perturb_landuse(src2, out2, lcz2, lcz_classes=(1,), fraction=0.8)
    with Dataset(out2) as ds:
        lu = ds["LANDUSEF"][0]
        assert np.allclose(lu[12, :, 0], 0.1) and np.allclose(lu[9, :, 0], 0.9), lu
        assert np.allclose(lu[12, :, 1], 0.5) and np.allclose(lu[9, :, 1], 0.5), lu
        assert np.allclose(lu.sum(axis=0), 1.0), lu
    print("counterfactual self-checks passed: LAI and land-use interventions")


if __name__ == "__main__":
    main()
