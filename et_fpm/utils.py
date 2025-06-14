"""Utility helpers."""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel
from dotenv import dotenv_values

from et_fpm import CONFIG_PATH


class Config(BaseModel):
    db_url: str
    lookback_window: int
    ewma_lambda: float
    stress_pct: int
    crisis_pct: int
    default_weight_scheme: str
    alert: dict


def load_config(path: Path | None = None) -> Config:
    """Load YAML configuration."""
    path = path or CONFIG_PATH / "config.yml"
    data = yaml.safe_load(Path(path).read_text())
    env = dotenv_values()
    if "alert" in data and "slack_webhook" in data["alert"]:
        data["alert"]["slack_webhook"] = env.get("SLACK_WEBHOOK", "")
    return Config(**data)
