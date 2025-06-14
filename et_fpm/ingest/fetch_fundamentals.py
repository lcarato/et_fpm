"""Fetch fundamentals like average daily volume."""

from __future__ import annotations

import pandas as pd


def fetch_adv(tickers: list[str]) -> pd.Series:
    """Return synthetic ADV for tickers."""
    return pd.Series(1_000_000, index=tickers)
