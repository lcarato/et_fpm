"""Market regime labelling and alerts."""

from __future__ import annotations

import pandas as pd


class IncompleteIngestError(Exception):
    """Raised when the ingest flow fails."""


def label_regime(trvi_series: pd.Series, stress_pct: int, crisis_pct: int) -> pd.Series:
    """Label market regimes based on TRVI percentiles."""
    stress = trvi_series.quantile(stress_pct / 100)
    crisis = trvi_series.quantile(crisis_pct / 100)

    def classify(x: float) -> str:
        if x >= crisis:
            return "crisis"
        if x >= stress:
            return "stress"
        return "normal"

    return trvi_series.apply(classify)
