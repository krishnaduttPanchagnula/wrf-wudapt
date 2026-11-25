"""Validation of WRF output against an independent point series.

The thesis called an interpolated gridded product "ground truth"; here we keep
the comparison explicit and report bias/RMSE/MAE with the sample size.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree


def load_era5(path: str | Path) -> pd.DataFrame:
    d = json.loads(Path(path).read_text())["hourly"]
    df = pd.DataFrame(d)
    df["time"] = pd.to_datetime(df["time"], utc=True)
    return df.set_index("time")


def wrf_nearest(ds, lat: float, lon: float, var: str) -> pd.Series:
    """Nearest grid cell to (lat, lon) in a WRF history file."""
    xlat = ds["XLAT"].isel(Time=0).values
    xlon = ds["XLONG"].isel(Time=0).values
    _, idx = cKDTree(np.column_stack([xlat.ravel(), xlon.ravel()])).query([lat, lon], k=1)
    iy, ix = np.unravel_index(int(idx), xlat.shape)
    from lcz_stats import wrf_times
    t = wrf_times(ds)
    vals = ds[var].values.reshape(-1, *xlat.shape)[:, iy, ix]
    return pd.Series(vals, index=t, name=var)


def score(model: pd.Series, obs: pd.Series) -> dict:
    a, b = model.align(obs, join="inner")
    if len(a) == 0:
        raise ValueError("no overlapping timestamps")
    d = a.to_numpy() - b.to_numpy()
    return {"n": int(len(a)), "bias": float(d.mean()), "mae": float(np.abs(d).mean()),
            "rmse": float(np.sqrt(np.mean(d**2)))}
