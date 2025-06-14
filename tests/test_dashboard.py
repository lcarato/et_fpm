from et_fpm.dashboard.app import load_data


def test_load_data():
    df = load_data()
    assert df.empty
