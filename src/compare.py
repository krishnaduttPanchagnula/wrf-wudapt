"""Compare two cases (e.g. two years) by LCZ and clock hour.

This is the function the QGIS plugin would call for its two-year comparison.
"""
import html
import math
from pathlib import Path

import numpy as np
import pandas as pd


def load_zonal(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["time"])
    df["time"] = pd.to_datetime(df["time"], utc=True)
    return df


def compare(a: pd.DataFrame, b: pd.DataFrame, var: str = "T2") -> pd.DataFrame:
    """Align two case outputs by LCZ, calendar day and hour, then difference."""
    def key(df: pd.DataFrame) -> pd.DataFrame:
        out = df[["LCZ", "time", var]].copy()
        out["date"] = out["time"].dt.strftime("%m-%d")
        out["hour"] = out["time"].dt.hour
        return out.drop(columns="time")

    m = key(a).merge(key(b), on=["LCZ", "date", "hour"], suffixes=("_a", "_b"))
    m[f"delta_{var}"] = m[f"{var}_b"] - m[f"{var}_a"]
    return m


def export_delta_geotiff(points: pd.DataFrame, path: str | Path) -> Path:
    """Write the mean ΔT2 grid as an EPSG:4326 GeoTIFF for GIS users.

    shortcut: the input CSV is a row-major flatten of a square WRF grid;
    upgrade to the XLAT/XLONG curvilinear grid when reprojection is needed.
    """
    import rasterio
    from rasterio.transform import from_origin

    n = len(points)
    side = int(math.isqrt(n))
    if side * side != n:
        raise ValueError("delta points must be a square grid")
    lat = points["lat"].to_numpy().reshape(side, side)
    lon = points["lon"].to_numpy().reshape(side, side)
    values = points["delta_T2_K"].to_numpy(dtype=np.float32).reshape(side, side)
    dx = float(np.mean(np.diff(lon[0])))
    dy = float(np.mean(np.diff(lat[:, 0])))
    profile = {"driver": "GTiff", "width": side, "height": side, "count": 1,
               "dtype": "float32", "crs": "EPSG:4326",
               "transform": from_origin(lon[0, 0] - dx / 2, lat[0, 0] + dy / 2, dx, dy),
               "nodata": -9999.0}
    path = Path(path)
    with rasterio.open(path, "w", **profile) as dst:
        dst.write(np.nan_to_num(values, nan=-9999.0), 1)
    return path


def side_by_side(a: pd.DataFrame, b: pd.DataFrame, var: str = "T2") -> pd.DataFrame:
    """Align a base and a proposal run into base / proposal / difference columns."""
    m = compare(a, b, var)
    return m.rename(columns={f"{var}_a": f"base_{var}",
                             f"{var}_b": f"proposal_{var}",
                             f"delta_{var}": "difference_K"})


def side_by_side_html(table: pd.DataFrame, validation: dict | None = None) -> str:
    """Render the hourly side-by-side table as a standalone HTML page."""
    cols = ["LCZ", "date", "hour", "base_T2", "proposal_T2", "difference_K"]
    rows = "".join(
        "<tr>" + "".join(f"<td>{html.escape(str(row[c]))}</td>" for c in cols) + "</tr>"
        for _, row in table[cols].iterrows())
    if validation:
        full = validation.get("full", {})
        held = validation.get("held_out_12_18Z", {})
        note = (f"{html.escape(str(validation.get('source', 'validation')))} — "
                f"n={full.get('n', '?')}, bias {full.get('bias', '?')} K, "
                f"RMSE {full.get('rmse', '?')} K; held-out RMSE "
                f"{held.get('rmse', '?')} K.")
    else:
        note = ("No validation metrics found beside this comparison — do not present "
                "it as a result (see CONSTRAINTS.md).")
    return f"""<!doctype html>
<meta charset="utf-8">
<title>Base / proposal / difference</title>
<style>body{{font:14px system-ui,sans-serif;margin:2rem;max-width:60rem}}
table{{border-collapse:collapse}}th,td{{padding:.3rem .7rem;border-bottom:1px solid #ddd;text-align:right}}
th{{background:#f2f2f2}}.warn{{color:#8a3b12}}</style>
<h1>Base / proposal / difference — T2 (K)</h1>
<p>Hour is UTC clock hour; calendar day is aligned. Difference = proposal − base.</p>
<table><thead><tr><th>LCZ</th><th>Date</th><th>Hour</th><th>Base (K)</th>
<th>Proposal (K)</th><th>Difference (K)</th></tr></thead><tbody>{rows}</tbody></table>
<p class="warn">{note}</p>
"""
