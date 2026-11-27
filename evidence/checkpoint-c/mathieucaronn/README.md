# Checkpoint C - Mathieu Caron

- GitHub: @mathieucaronn
- Team: G01 - T3M
- Final provider: Bloomberg stage - `APPROVED_SAMPLE` (instructor-approved sample, no live Bloomberg connectivity)

## Evidence

- `01_final_market_data.png`: `python src/main.py` on the final team `main`: Bloomberg stage / APPROVED_SAMPLE, 1 month, Daily, AAPL +6.48%, SP500 +2.15%, AAPL vs SP500 +4.33 percentage points.
- `02_dash_dashboard.png`: final team dashboard (`python src/dashboard.py`): context, three performance indicators and base-100 chart for AAPL and SP500.
- `03_final_pull_request.png`: [my TD10 PR #29 - feat: add Bloomberg provider boundary](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/29), closed without merge; the team kept Matthieu Labbé's provider (PR #22).
- `04_reproducible_run.png`: fresh clone `~/marketpulse-repro` of the team repository, `python -m pip install -r requirements.txt` and a successful `python src/main.py`.

## My TD09-TD12 Pull Requests

- [#27 - docs: map Bloomberg stage to MarketPulse](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/27) (TD09), closed; team kept PR #17.
- [#29 - feat: add Bloomberg provider boundary](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/29) (TD10), closed; team kept PR #22.
- [#37 - feat: add MarketPulse Dash dashboard](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/37) (TD11), closed; team kept PR #31.
- [#41 - chore: prepare MarketPulse final release](https://github.com/matthcab/esilv-marketpulse-g01-t3M/pull/41) (TD12), closed; team final integration is PR #36.

## Notes

- The screenshots show the final merged team version, not my closed PRs presented as merged.
- The reproducible run reused the Anaconda Python environment, so `pip` reported the dependencies as already satisfied; the clone itself was fresh.
- No secret appears in the screenshots.
