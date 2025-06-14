# ET-FPM

Energy-Transition Financial Performance Monitor (ET-FPM) is a demonstration platform tracking market prices and fundamentals across the energy transition. It calculates risk metrics like the Transition Risk Volatility Index (TRVI), Sharpe ratios, and regime states to help analyze sector stress. Data is ingested daily via Prefect, stored in TimescaleDB, and displayed in a Streamlit dashboard. Weekly PDF reports summarize recent performance. **Demo only; users must secure proper market-data rights.**

## Quick Start

```bash
poetry install
cp .env.example .env  # fill in secrets
python -m et_fpm.dashboard.app
```

## Weight Schemes

Weight modules live in `et_fpm/weights/`. Add new schemes following the pattern in `utils.py` and reference them in `config/config.yml` under `default_weight_scheme`.

## License

MIT License. See [LICENSE](LICENSE).
