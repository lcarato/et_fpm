"""Factor models."""

from __future__ import annotations

import pandas as pd
import statsmodels.api as sm


def rolling_beta(asset_ret: pd.Series, factor_ret: pd.Series, window: int) -> pd.Series:
    """Rolling beta via OLS."""
    betas = []
    for i in range(window, len(asset_ret) + 1):
        y = asset_ret.iloc[i - window : i]
        x = sm.add_constant(factor_ret.iloc[i - window : i])
        res = sm.OLS(y, x).fit()
        betas.append(res.params[1])
    return pd.Series(betas, index=asset_ret.index[window - 1 :])


def rolling_alpha(asset_ret: pd.Series, factor_ret: pd.Series, window: int) -> pd.Series:
    """Rolling alpha via OLS."""
    alphas = []
    for i in range(window, len(asset_ret) + 1):
        y = asset_ret.iloc[i - window : i]
        x = sm.add_constant(factor_ret.iloc[i - window : i])
        res = sm.OLS(y, x).fit()
        alphas.append(res.params[0])
    return pd.Series(alphas, index=asset_ret.index[window - 1 :])
