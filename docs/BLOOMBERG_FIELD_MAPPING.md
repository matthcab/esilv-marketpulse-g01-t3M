# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

- Source: `data/sample/bloomberg_reference_sample.json`
- Reference: `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md` (not present in the team repository)
- Live connectivity: not demonstrated (no Bloomberg terminal access during the session)

The sample declares `"is_live_bloomberg_output": false`. Its values are teaching values reused from `data/sample/prices.csv`, not certified Bloomberg observations.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | teaching wrapper key; text `YYYY-MM-DD` |
| ticker | application mapping from `canonical_ticker` | AAPL or SP500, never the Bloomberg identifier |
| open | `open_value` | teaching wrapper key; convert to float |
| high | `high_value` | teaching wrapper key; convert to float |
| low | `low_value` | teaching wrapper key; convert to float |
| close | `close_value` | teaching wrapper key; convert to float |
| volume | `volume_value` | teaching wrapper key; convert to int; 0 for SP500 |

Important: teaching wrapper key != Bloomberg LIVE field mnemonic.
No real Bloomberg field name was observed or invented in this document.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity -> AAPL
- Benchmark identifier: SPX Index -> SP500
- Date representation: text `YYYY-MM-DD` in `observation_date`
- Input structure: JSON object with a `series` list; each series has `role`, `canonical_ticker`, `provider_identifier` and an `observations` list
- Missing fields: none in the sample; 21 observations per series (2026-09-01 to 2026-09-30)
- Special normalization notes: some prices are integers in the JSON (e.g. 248, 6600) and must be converted to float; SP500 volume is 0; the row ticker must be the canonical ticker
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`