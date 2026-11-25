"""ML emulator for WRF-derived zonal temperature.

Not a replacement for physics: it emulates an ensemble of *counterfactual WRF
runs*, never a correlation fitted to one baseline run. Monotonic constraints
encode the physics we trust (more vegetation / soil moisture cannot warm air).
"""
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GroupKFold


@dataclass
class Emulator:
    features: list[str]
    target: str
    monotone: dict[str, int]  # feature -> -1 (must not increase target), +1, or 0
    model: HistGradientBoostingRegressor | None = None
    train_range: dict[str, tuple[float, float]] | None = None

    def fit(self, df: pd.DataFrame) -> "Emulator":
        X = df[self.features]
        y = df[self.target]
        self.train_range = {c: (float(X[c].min()), float(X[c].max())) for c in self.features}
        cst = [self.monotone.get(c, 0) for c in self.features]
        self.model = HistGradientBoostingRegressor(
            monotonic_cst=cst, max_iter=200, learning_rate=0.06,
            max_leaf_nodes=15, min_samples_leaf=8, l2_regularization=1.0,
            random_state=42,
        ).fit(X, y)
        return self

    def predict(self, df: pd.DataFrame, check_support: bool = True) -> np.ndarray:
        if self.model is None:
            raise RuntimeError("fit() first")
        X = df[self.features]
        if check_support:
            self.assert_supported(X)
        return self.model.predict(X)

    def assert_supported(self, X: pd.DataFrame) -> None:
        """Scenarios outside training support are extrapolations, not predictions."""
        for c, (lo, hi) in self.train_range.items():
            tol = 1e-9 * max(1.0, abs(lo), abs(hi))
            if X[c].min() < lo - tol or X[c].max() > hi + tol:
                raise ValueError(
                    f"{c}: scenario values [{X[c].min():.3g}, {X[c].max():.3g}] "
                    f"outside training support [{lo:.3g}, {hi:.3g}]. "
                    "Run WRF at those values instead of extrapolating."
                )


def blocked_score(df: pd.DataFrame, emu: Emulator, group_col: str = "lcz") -> dict:
    """GroupKFold by LCZ: no LCZ used in training may appear in the test fold.

    Random splitting would leak the diurnal cycle and inflate skill.
    """
    gaps = []
    n_splits = min(5, df[group_col].nunique())
    for train, test in GroupKFold(n_splits=n_splits).split(df, groups=df[group_col]):
        m = emu.__class__(emu.features, emu.target, emu.monotone).fit(df.iloc[train])
        # Held-out observations are validation, not scenarios: support is enforced
        # at scenario-prediction time, not against an arbitrary CV fold.
        pred = m.model.predict(df.iloc[test][emu.features])
        gaps.append((df.iloc[test][emu.target].to_numpy(), pred))
    y = np.concatenate([g[0] for g in gaps])
    p = np.concatenate([g[1] for g in gaps])
    naive = np.full_like(y, df[emu.target].mean())  # climatology baseline
    return {
        "rmse": float(np.sqrt(mean_squared_error(y, p))),
        "mae": float(mean_absolute_error(y, p)),
        "r2": float(r2_score(y, p)),
        "naive_rmse": float(np.sqrt(mean_squared_error(y, naive))),
    }
