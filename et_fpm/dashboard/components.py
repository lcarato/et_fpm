"""Streamlit components."""

from __future__ import annotations

import streamlit as st


def kpi_card(title: str, value: float) -> None:
    """Render a KPI card."""
    st.metric(title, f"{value:.2f}")
