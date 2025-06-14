"""ET-FPM package initialization."""

from pathlib import Path

__version__ = "0.1.0"
PACKAGE_PATH = Path(__file__).resolve().parent
DATA_PATH = PACKAGE_PATH.parent / "data"
CONFIG_PATH = PACKAGE_PATH.parent / "config"
