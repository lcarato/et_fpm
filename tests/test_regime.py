import pandas as pd

from et_fpm.analytics.regime import label_regime


def test_label_regime():
    s = pd.Series([1, 2, 3, 4, 5])
    labels = label_regime(s, 50, 80)
    assert labels.iloc[-1] == "crisis"
    assert labels.iloc[0] == "normal"
