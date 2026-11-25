"""Clip the European LCZ map to Milan and reproject to EPSG:4326 for w2w."""
from pathlib import Path

import numpy as np
import rasterio
from pyproj import Transformer
from rasterio.warp import Resampling, calculate_default_transform, reproject
from rasterio.windows import from_bounds

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/raw/lcz_europe.tif"
DST = ROOT / "data/raw/lcz_europe_4326.tif"
LON, LAT = 9.16646, 45.4937
HALF_M = 250_000  # 500 km square, comfortably larger than the 3 km inner domain


def main() -> None:
    x, y = Transformer.from_crs("EPSG:4326", "EPSG:3035", always_xy=True).transform(LON, LAT)
    bounds = (x - HALF_M, y - HALF_M, x + HALF_M, y + HALF_M)
    with rasterio.open(SRC) as ds:
        win = from_bounds(*bounds, transform=ds.transform)
        data = ds.read(window=win)
        transform = ds.window_transform(win)
        profile = ds.profile.copy()
    profile.update({"width": data.shape[2], "height": data.shape[1], "transform": transform})
    profile = {k: v for k, v in profile.items() if k != "driver"}
    with rasterio.MemoryFile() as mf:
        with mf.open(driver="GTiff", **profile) as src:
            src.write(data)
            dt, dw, dh = calculate_default_transform(
                src.crs, "EPSG:4326", src.width, src.height, *src.bounds)
            out_profile = src.profile.copy()
            out_profile.update({"crs": "EPSG:4326", "transform": dt, "width": dw, "height": dh})
            with rasterio.open(DST, "w", **out_profile) as dst:
                reproject(
                    source=rasterio.band(src, 1), destination=rasterio.band(dst, 1),
                    src_transform=src.transform, src_crs=src.crs,
                    dst_transform=dt, dst_crs="EPSG:4326", resampling=Resampling.nearest)
    print(f"wrote {DST}: {dw}x{dh}, EPSG:4326")


if __name__ == "__main__":
    main()
