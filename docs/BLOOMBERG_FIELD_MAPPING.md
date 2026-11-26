# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

- Source: `data/sample/bloomberg_reference_sample.json`
- Reference: `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md` (not present in the team repository)
- Live connectivity: not demonstrated (no Bloomberg terminal access during the session)

The sample itself declares `"access_mode": "approved_sample"` and `"is_live_bloomberg_output": false`.
Its values are teaching values reused from `data/sample/prices.csv`, not certified Bloomberg observations.
This document must not be presented as proof of LIVE Bloomberg connectivity.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

Inspected in the sample (`series` list):

| `role` | `canonical_ticker` | `provider_identifier` | Observations |
|---|---|---|---|
| instrument | AAPL | AAPL US Equity | 21 |
| benchmark | SP500 | SPX Index | 21 |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | teaching wrapper key; text `YYYY-MM-DD`, kept as is |
| ticker | application mapping from the series `canonical_ticker` | `AAPL` or `SP500`, never the Bloomberg identifier |
| open | `open_value` | teaching wrapper key; convert to `float` |
| high | `high_value` | teaching wrapper key; convert to `float` |
| low | `low_value` | teaching wrapper key; convert to `float` |
| close | `close_value` | teaching wrapper key; convert to `float` |
| volume | `volume_value` | teaching wrapper key; convert to `int`; `0` for SP500 |

Important:

```text
teaching wrapper key (observation_date, close_value, ...)
!=
Bloomberg LIVE field mnemonic
```

No LIVE Bloomberg field name is listed here, because none was observed.

## Canonical tickers

The provider identifier stops at the provider boundary.
Normalized rows must use the canonical tickers, for example:

```python
{
    "date": "2026-09-01",
    "ticker": "SP500",        # not "SPX Index"
    "open": 6592.0,
    "high": 6615.0,
    "low": 6580.0,
    "close": 6600.0,
    "volume": 0,
}
```

`src/analytics.py` keeps receiving `AAPL` and `SP500` only.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: `AAPL US Equity` -> canonical `AAPL`
- Benchmark identifier: `SPX Index` -> canonical `SP500`
- Date representation: string `YYYY-MM-DD` in `observation_date`
- Input structure: JSON object with a `series` list; each series has `role`, `canonical_ticker`, `provider_identifier` and an `observations` list
- Missing fields: none in the sample; SP500 `volume_value` is `0` (an index has no traded volume)
- Special normalization notes: open/high/low/close may be integers in the JSON (e.g. `6600`), so always convert with `float()`; volume with `int()`
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
