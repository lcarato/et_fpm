"""Database initialization helpers."""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from et_fpm.db.models import metadata


def get_engine(url: str) -> Engine:
    """Create an SQLAlchemy engine."""
    return create_engine(url, echo=False, future=True)


def init_db(engine: Engine) -> None:
    """Create tables."""
    metadata.create_all(engine)
