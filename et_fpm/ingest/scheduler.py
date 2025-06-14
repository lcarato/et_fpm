"""Prefect flows for ingestion and reporting."""

from __future__ import annotations

from prefect import flow, task
from prefect.tasks import task_input_hash
from prefect.schedules import CronSchedule

from et_fpm.assets import ALL_TICKERS
from et_fpm.analytics.regime import IncompleteIngestError
from et_fpm.db.init_db import get_engine
from et_fpm.ingest.fetch_prices import ingest_prices
from et_fpm.utils import load_config


@task(retries=3, retry_delay_seconds=60, persist_result=False, cache_key_fn=task_input_hash)
def fetch_task() -> int:
    cfg = load_config()
    engine = get_engine(cfg.db_url)
    return ingest_prices(engine)


@flow(name="daily_ingest", retries=0)
def daily_ingest() -> None:
    """Run daily price ingestion."""
    ingested = fetch_task()
    if ingested / len(ALL_TICKERS) < 0.8:
        raise IncompleteIngestError(f"only {ingested} tickers ingested")


schedule = CronSchedule(cron="0 21 * * *", timezone="America/Argentina/Buenos_Aires")
