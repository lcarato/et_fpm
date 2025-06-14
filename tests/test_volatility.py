import pandas as pd

from et_fpm.analytics.volatility import calc_trvi, ewma_sigma


def test_calc_trvi():
    df = pd.DataFrame({"a": [0.01, 0.02], "b": [0.03, 0.04]})
    w = pd.Series([0.5, 0.5], index=["a", "b"])
    val = calc_trvi(df, w)
    assert val > 0


def test_ewma_sigma():
    s = pd.Series([0.01, 0.02, -0.01])
    sigma = ewma_sigma(s, 0.5)
    assert sigma > 0
