"""Self-checks for the emulator. Run: ./run.sh run 'python tests/test_emulator.py'"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from emulator import Emulator, blocked_score  # noqa: E402


def main() -> None:
    rng = np.random.default_rng(0)
    n = 400
    lai = rng.uniform(2.7, 2.9, n)
    soil = rng.uniform(0.28, 0.32, n)
    y = 308 - 20 * (lai - 2.7) - 5 * (soil - 0.28) + rng.normal(0, 0.02, n)
    df = pd.DataFrame({"lai": lai, "soil": soil, "temp": y,
                       "lcz": rng.integers(1, 18, n)})

    emu = Emulator(["lai", "soil"], "temp", {"lai": -1, "soil": -1}).fit(df)

    # Physics: more leaves/soil moisture may never increase predicted temperature.
    grid = pd.DataFrame({"lai": np.linspace(df.lai.min(), df.lai.max(), 25),
                         "soil": np.full(25, 0.30)})
    p = emu.predict(grid)
    assert np.all(np.diff(p) <= 1e-9), f"LAI monotonicity broken: {np.diff(p).max()}"

    # No extrapolation: a scenario outside training support must be rejected.
    try:
        emu.predict(pd.DataFrame({"lai": [3.5], "soil": [0.30]}))
    except ValueError:
        pass
    else:
        raise AssertionError("out-of-support scenario was not rejected")

    # Leakage-safe score must be finite and beat the climatology baseline.
    s = blocked_score(df, emu)
    assert np.isfinite(s["rmse"]) and s["rmse"] < s["naive_rmse"], s
    print("emulator self-checks passed:", s)


if __name__ == "__main__":
    main()
