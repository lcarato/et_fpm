"""Volatility calculations."""

from __future__ import annotations

import numpy as np
import pandas as pd


def calc_trvi(ret_df: pd.DataFrame, weights: pd.Series) -> pd.Series:
    """Compute Transition Risk Volatility Index."""
    cov = ret_df.cov()
    return np.sqrt(weights.T @ cov @ weights)


def ewma_sigma(series: pd.Series, lam: float) -> float:
    """Exponential-weighted volatility."""
    weights = np.power(lam, np.arange(len(series))[::-1])
    weights /= weights.sum()
    return np.sqrt(np.sum(weights * series**2))
