"""Positive Sharpe scaling weights."""

from __future__ import annotations

import pandas as pd


def weight(sharpes: pd.Series) -> pd.Series:
    """Scale weights by positive Sharpe ratios."""
    pos = sharpes.clip(lower=0)
    if pos.sum() == 0:
        return pd.Series(1 / len(pos), index=pos.index)
    return pos / pos.sum()
