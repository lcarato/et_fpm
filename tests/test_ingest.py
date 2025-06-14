import pandas as pd
import sqlalchemy as sa
from et_fpm.db.init_db import init_db, get_engine

from et_fpm.ingest.fetch_prices import ingest_prices


def test_ingest_prices(monkeypatch):
    engine = get_engine("sqlite:///:memory:")
    init_db(engine)

    def fake_fetch(ticker):
        idx = pd.date_range("2024-01-01", periods=3, tz="UTC")
        return pd.Series([1, 2, 3], index=idx)

    monkeypatch.setattr("et_fpm.ingest.fetch_prices.fetch_price_series", fake_fetch)
    count = ingest_prices(engine, tickers=["AAA"])
    assert count == 1
    with engine.connect() as conn:
        result = conn.execute(sa.text("select count(*) from prices")).scalar()
    assert result == 3
