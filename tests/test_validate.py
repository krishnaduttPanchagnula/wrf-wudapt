"""Self-checks for validation metrics. Run: ./run.sh run 'python tests/test_validate.py'"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from validate import score  # noqa: E402


def main() -> None:
    t = pd.date_range("2022-07-25", periods=24, freq="h", tz="UTC")
    obs = pd.Series(303.0 + np.sin(np.arange(24) / 24 * 2 * np.pi), index=t)
    model = obs + 0.5  # constant warm bias
    s = score(model, obs)
    assert s["n"] == 24
    assert abs(s["bias"] - 0.5) < 1e-9, s
    assert abs(s["rmse"] - 0.5) < 1e-9, s
    assert score(model, obs.iloc[:12])["n"] == 12  # inner join on time
    print("validation self-checks passed:", s)


if __name__ == "__main__":
    main()
