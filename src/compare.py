"""Compare two cases (e.g. two years) by LCZ and clock hour.

This is the function the QGIS plugin would call for its two-year comparison.
"""
from pathlib import Path

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
