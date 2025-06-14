"""Liquidity-inverse weight scheme."""

from __future__ import annotations

import pandas as pd


def weight(tickers: list[str], adv: pd.Series) -> pd.Series:
    """Weights proportional to inverse ADV."""
    inv = 1 / adv.reindex(tickers)
    inv = inv.fillna(inv.mean())
    return inv / inv.sum()
