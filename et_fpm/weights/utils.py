"""Weight scheme registry."""

from __future__ import annotations

from importlib import import_module
from typing import Any, Callable


_REGISTRY: dict[str, Callable[..., Any]] = {
    "liq_inv": lambda **k: import_module("et_fpm.weights.liq_inv").weight(**k),
    "sharpe_pos": lambda **k: import_module("et_fpm.weights.sharpe_pos").weight(**k),
}


def get_weights(scheme: str, **kwargs: Any) -> Any:
    """Return weights for a scheme."""
    if scheme not in _REGISTRY:
        raise ValueError(f"unknown scheme {scheme}")
    return _REGISTRY[scheme](**kwargs)
