"""Streamlit dashboard app."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from et_fpm.analytics.volatility import calc_trvi
from et_fpm.analytics.sharpe import rolling_sharpe
from et_fpm.dashboard.components import kpi_card


@st.cache_data
def load_data() -> pd.DataFrame:
    """Load price data from CSV placeholder."""
    return pd.DataFrame()


def main() -> None:
    """Run dashboard UI."""
    st.title("ET-FPM Dashboard")
    df = load_data()
    if df.empty:
        st.info("No data available")
        return

    ret = df.pct_change().dropna()
    trvi = calc_trvi(ret, pd.Series(1 / len(ret.columns), index=ret.columns))
    kpi_card("TRVI", float(trvi))

    sharpe = rolling_sharpe(ret.mean(axis=1), pd.Series(0, index=ret.index))
    kpi_card("Mean Sharpe", sharpe.iloc[-1])

    if st.sidebar.button("Refresh"):
        st.cache_data.clear()

    st.write("Data-licensing disclaimer: demo only")


if __name__ == "__main__":
    main()
