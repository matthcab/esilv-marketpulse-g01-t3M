# ESILV MarketPulse - Team G01-T3M

MarketPulse compares one instrument with its benchmark over the same period and frequency (in our case, we compare Apple stock with the S&P 500).

## Market comparison

- Instrument: AAPL - Apple Inc.
- Benchmark: S&P 500 (SP500)
- Lookback: 1 month
- Interval: Daily
- Metrics: period return, base 100, relative performance

## Provider used in the final release

Bloomberg stage - APPROVED_SAMPLE

- No Bloomberg terminal was available, so the Bloomberg provider reads the instructor-approved sample `data/sample/bloomberg_reference_sample.json`.
- This mode validates the provider boundary and normalization. It does not prove live Bloomberg connectivity.
- A Yahoo Finance provider (`src/providers/yahoo_provider.py`, via yfinance) is also available from TD08.

## Installation

Python 3 is required.

```bash
python -m pip install -r requirements.txt
```

## Run

Terminal:

```bash
python src/main.py
```

Dashboard:

```bash
python src/dashboard.py
```

Then open http://127.0.0.1:8050/ in a browser.

Run both commands from the repository root. If `python` is not found (macOS), use `python3`.

## Project structure

```text
src/
├── main.py                 # orchestration, build_market_snapshot(), terminal output
├── analytics.py            # alignment, period return, base 100, relative performance
├── dashboard.py            # Dash presentation of the shared snapshot
└── providers/
    ├── yahoo_provider.py
    └── bloomberg_provider.py
```

## Documentation and evidence

- Bloomberg mapping: `docs/BLOOMBERG_FIELD_MAPPING.md`
- Checkpoint evidence: `evidence/checkpoint-a/`, `evidence/checkpoint-b/`, `evidence/checkpoint-c/`
- TP reports: `rendu_TP/<student>/`
- Team: `Team.md`