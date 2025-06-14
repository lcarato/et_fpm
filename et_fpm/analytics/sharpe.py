"""Sharpe ratio calculations."""

from __future__ import annotations

import numpy as np
import pandas as pd


def rolling_sharpe(series: pd.Series, rf: pd.Series) -> pd.Series:
    """Rolling Sharpe ratio using 252-day annualisation."""
    excess = series - rf.reindex_like(series)
    return excess.rolling(252).mean() / excess.rolling(252).std() * np.sqrt(252)
