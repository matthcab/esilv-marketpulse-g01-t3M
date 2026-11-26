# Checkpoint B - Mathieu Caron

- GitHub: @mathieucaronn
- Team: G01 - T3M

## Pull Requests

- [PR #4 - feat: display market metadata](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/4) (TD05): reviewed and approved by @matthieulbb, merged into `main`.
- [PR #19 - feat: add Yahoo Finance provider](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/19) (TD08): closed without merge, the team kept Matthieu Labbé's implementation ([PR #12](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/12)).
- TD07 done individually on branch [`rendu/td07-caron`](https://github.com/matthcab/esilv-marketpulse-g01-t3M/tree/rendu/td07-caron) (commit `800eacd`), no PR because the team TD07 was already merged ([PR #8](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/8)).

## Code review

- [PR #1 - docs: clarify how to run MarketPulse](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/1) (TD06): approved after checking the README instructions against the code (relative `data/sample` path, standard-library-only imports, expected output).

## Evidence

- `01_pull_request.png`: my TD08 Pull Request #19.
- `02_code_review.png`: my approval review on PR #1.
- `03_yahoo_market_data.png`: AAPL and SP500 (`^GSPC`) retrieved live from Yahoo Finance as canonical MarketPulse rows.
- `04_instrument_benchmark.png`: `python src/main.py` with Yahoo Finance, 1 month, Daily: AAPL vs SP500 period returns, relative performance and base 100.

## Validation

- `python src/main.py` runs with provider "Yahoo Finance via yfinance".
- AAPL and SP500 both return 23 daily rows, aligned on the same dates.
- Base 100 starts at 100.00 for both series; relative performance = instrument return - benchmark return.
