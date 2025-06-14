"""Database models."""

from sqlalchemy import Column, DateTime, Float, MetaData, String, Table

metadata = MetaData()

prices = Table(
    "prices",
    metadata,
    Column("ts", DateTime(timezone=True), primary_key=True),
    Column("ticker", String, primary_key=True),
    Column("price", Float),
    Column("source", String),
)
