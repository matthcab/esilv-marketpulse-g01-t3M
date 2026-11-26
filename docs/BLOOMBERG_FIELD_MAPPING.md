# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

Input file: `data/sample/bloomberg_reference_sample.json`  
Expected output: `data/sample/bloomberg_reference_expected.json`  
Instructor reference listed in TD09: `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md`

The input contains illustrative teaching data. Its observation keys belong
to the teaching fixture. Live Bloomberg connectivity and live field names
were not verified in this session.

## Market instruments

| Role | MarketPulse ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source in the sample JSON | Rule |
|---|---|---|
| date | `observation_date` | Keep the date in `YYYY-MM-DD` format. |
| ticker | `canonical_ticker` on the parent series | Copy `AAPL` or `SP500` to each row. |
| open | `open_value` | Copy the opening value. |
| high | `high_value` | Copy the daily high. |
| low | `low_value` | Copy the daily low. |
| close | `close_value` | Copy the closing value. |
| volume | `volume_value` | Copy the volume, including zero. |

## TD10 handoff

Read the `series` array. For each series, read its `canonical_ticker`
and produce one MarketPulse row per entry in `observations`.

Each series contains 21 observations from 2026-09-01 to 2026-09-30.
All required fields are present. On 2026-09-01, AAPL closes at 250
with volume 38000000. SP500 closes at 6600 with volume 0.
Keep that zero in the output.

Applying the field mapping reproduces all 42 rows in
`data/sample/bloomberg_reference_expected.json`.