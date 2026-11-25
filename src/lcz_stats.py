"""Aggregate WRF output by LCZ class.

The LCZ map drives urban extent in WRF via w2w. This build cannot ingest the
41-category LCZ field (see README shortcut), so the class labels used for
sampling are read from the same LCZ GeoTIFF at the model grid points.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import xarray as xr

DEFAULT_VARS = ("T2", "U10", "V10", "LH", "HFX", "ALBEDO", "SMSTAV", "UTCI")


def sample_lcz(wrfinput: str | Path, lcz_tif: str | Path) -> np.ndarray:
    """Sample LCZ classes from the source GeoTIFF at the model grid coordinates."""
    import rasterio

    with xr.open_dataset(wrfinput) as st:
        shape = st["XLAT"].isel(Time=0).shape
        lat = st["XLAT"].isel(Time=0).values.ravel()
        lon = st["XLONG"].isel(Time=0).values.ravel()
    with rasterio.open(lcz_tif) as src:
        vals = np.fromiter(
            (v[0] for v in src.sample(zip(lon, lat), indexes=1)),
            dtype=np.int16, count=len(lat),
        )
    return vals.reshape(shape)


def wrf_times(ds) -> pd.DatetimeIndex:
    raw = np.asarray(ds["Times"].values)
    n = raw.shape[0]
    if raw.dtype.kind in "US":
        names = raw.reshape(n, -1).astype(str)
        names = np.array(["".join(row).strip() for row in names])
    else:
        names = np.array(["".join(c).strip() for c in raw.reshape(n, -1)])
    return pd.to_datetime([s.replace("_", " ") for s in names], utc=True)


def zonal_stats(wrfout: str | Path, wrfinput: str | Path,
                variables=DEFAULT_VARS, domain: int = 2,
                lcz_tif: str | Path | None = None,
                lcz: np.ndarray | None = None) -> pd.DataFrame:
    with xr.open_dataset(wrfinput) as static:
        if lcz is None:
            lcz = (static["LCZ"].isel(Time=0).values if "LCZ" in static
                   else sample_lcz(wrfinput, lcz_tif) if lcz_tif
                   else None)
    if lcz is None:
        raise ValueError("no LCZ field in wrfinput: pass lcz_tif or lcz")
    lcz = np.asarray(lcz)

    rows = []
    with xr.open_dataset(wrfout) as ds:
        times = wrf_times(ds)
        for i, t in enumerate(times):
            vals = {}
            for v in variables:
                if v == "UTCI":
                    from heat_index import utci_from_wrf
                    vals["UTCI"] = utci_from_wrf(ds, i).ravel()
                    continue
                if v not in ds:
                    continue
                a = ds[v].isel(Time=i).values
                if a.ndim == 2 and a.shape == lcz.shape:
                    vals[v] = a.ravel()
            if not vals:
                continue
            frame = pd.DataFrame({**vals, "LCZ": lcz.ravel()})
            frame = frame[frame["LCZ"] > 0]  # nodata / outside the LCZ map
            agg = frame.groupby("LCZ").mean(numeric_only=True)
            agg["time"], agg["domain"] = t, domain
            rows.append(agg.reset_index())
    if not rows:
        return pd.DataFrame()
    out = pd.concat(rows, ignore_index=True)
    return out[["time", "domain", "LCZ", *[v for v in variables if v in out]]]
