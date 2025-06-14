"""Price ingestion utilities."""

from __future__ import annotations

import pandas as pd
import yfinance as yf
from sqlalchemy import insert
from sqlalchemy.engine import Engine

from et_fpm.assets import ALL_TICKERS
from et_fpm.db.models import prices


def fetch_price_series(ticker: str) -> pd.Series:
    """Fetch adjusted daily prices for a ticker."""
    data = yf.download(ticker, auto_adjust=True, progress=False)
    if data.empty:
        return pd.Series(dtype="float64")
    series = data["Close"].drop_duplicates().sort_index()
    series.index = pd.to_datetime(series.index, utc=True).normalize()
    series = series.ffill()
    return series


def ingest_prices(engine: Engine, tickers: list[str] | None = None) -> int:
    """Fetch prices and insert into the database."""
    tickers = tickers or ALL_TICKERS
    success = 0
    for tkr in tickers:
        series = fetch_price_series(tkr)
        if series.empty:
            continue
        records = [
            {"ts": dt.to_pydatetime(), "ticker": tkr, "price": float(val), "source": "yfinance"}
            for dt, val in series.items()
        ]
        with engine.begin() as conn:
            conn.execute(insert(prices), records)
        success += 1
    return success
