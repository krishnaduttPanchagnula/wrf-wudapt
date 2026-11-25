"""Self-checks for two-case comparison."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from compare import compare  # noqa: E402


def main() -> None:
    t = pd.date_range("2022-07-25", periods=4, freq="h", tz="UTC")
    a = pd.DataFrame({"LCZ": [1, 1, 2, 2], "time": t, "T2": np.full(4, 300.0)})
    b = a.copy()
    b["T2"] = np.array([300.5, 300.5, 299.0, 299.0])
    b["time"] = t + pd.DateOffset(years=1)  # same calendar day, next year
    m = compare(a, b)
    assert len(m) == 4 and set(m["LCZ"]) == {1, 2}
    assert np.allclose(m.loc[m.LCZ == 1, "delta_T2"], 0.5)
    assert np.allclose(m.loc[m.LCZ == 2, "delta_T2"], -1.0)
    print("two-case comparison self-checks passed")


if __name__ == "__main__":
    main()
