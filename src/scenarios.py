"""Counterfactual initial states for WRF.

The thesis changed LAI in a regression fitted to the baseline run -- that is not
a physical intervention. Here we change the land-surface field in wrfinput and
re-run WRF, so the response includes evapotranspiration/radiation/turbulence
feedbacks.
"""
from pathlib import Path

import numpy as np
import xarray as xr


def perturb_landuse(wrfinput: str | Path, out: str | Path, lcz: np.ndarray,
                    lcz_classes: tuple[int, ...], from_cat: int = 13,
                    to_cat: int = 10, fraction: float = 0.8) -> Path:
    """Replace part of the urban land-use fraction with grassland in given LCZs.

    Noah derives LAI, albedo and roughness from land use, so editing the initial
    LAI field alone has no effect on WRF. This changes the field WRF actually
    reads. The total land-use fraction is conserved.
    """
    with xr.open_dataset(wrfinput) as ds:
        modified = ds.copy(deep=True)
        lu = modified["LANDUSEF"].values
        mask = np.isin(np.asarray(lcz), lcz_classes)
        src, dst = lu[:, from_cat - 1], lu[:, to_cat - 1]
        moved = np.minimum(src[:, mask], fraction * src[:, mask])
        src[:, mask] -= moved
        dst[:, mask] += moved
        lu_index = modified["LU_INDEX"].values
        lu_index[:, mask] = lu[:, :, mask].argmax(axis=1) + 1
        modified.to_netcdf(out)
    return Path(out)


def perturb_lai(wrfinput: str | Path, out: str | Path, factor: float,
                lcz_classes: tuple[int, ...] | None = None,
                lcz: np.ndarray | None = None) -> Path:
    """Scale initial LAI by factor, optionally only in chosen LCZ classes.

    ``lcz`` supplies the sampled LCZ grid when WRF has no LCZ field in wrfinput
    (the current build).
    """
    with xr.open_dataset(wrfinput) as ds:
        modified = ds.copy(deep=True)
        if "LAI" not in modified:
            raise ValueError("wrfinput has no LAI field")
        mask = np.ones(modified["LAI"].shape[-2:], dtype=bool)
        if lcz_classes:
            if lcz is None:
                lcz = modified["LCZ"].isel(Time=0).values
            mask = np.isin(np.asarray(lcz), lcz_classes)
        vals = modified["LAI"].values
        # LAI has Time, south_north, west_east; apply the 2-D mask to every time.
        vals[:, mask] = vals[:, mask] * factor
        modified.to_netcdf(out)
    return Path(out)


def perturb_soil(wrfinput: str | Path, out: str | Path, factor: float) -> Path:
    """Scale initial volumetric soil moisture (SMOIS) in wrfinput."""
    with xr.open_dataset(wrfinput) as ds:
        modified = ds.copy(deep=True)
        if "SMOIS" not in modified:
            raise ValueError("wrfinput has no SMOIS field")
        modified["SMOIS"].values = modified["SMOIS"].values * factor
        modified.to_netcdf(out)
    return Path(out)
