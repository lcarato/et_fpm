"""Supply chain correlation analysis."""

from __future__ import annotations

import json
from typing import Dict

import pandas as pd


def correlation_matrix(levels: Dict[str, list[str]], price_df: pd.DataFrame) -> pd.DataFrame:
    """Create a correlation matrix for supply chain levels."""
    subset = price_df[sum(levels.values(), [])]
    return subset.pct_change().corr()


def sankey_data(corr: pd.DataFrame) -> str:
    """Convert correlation matrix to Sankey-ready JSON."""
    links = []
    for i, src in enumerate(corr.columns):
        for j, tgt in enumerate(corr.index):
            if i >= j:
                continue
            links.append({"source": src, "target": tgt, "value": float(corr.iloc[j, i])})
    return json.dumps({"links": links})
