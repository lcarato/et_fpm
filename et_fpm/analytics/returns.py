"""Return calculations."""

from __future__ import annotations
import numpy as np

import pandas as pd


def get_returns(df: pd.DataFrame, method: str = "log") -> pd.DataFrame:
    """Compute daily returns from a price DataFrame."""
    if method == "log":
        return pd.DataFrame(np.log(df / df.shift(1))).dropna()
    raise ValueError("method must be 'log'")
