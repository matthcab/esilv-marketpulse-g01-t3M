"""Bloomberg-stage provider.

Access mode: APPROVED_SAMPLE (see docs/BLOOMBERG_FIELD_MAPPING.md).
Raw input comes from the instructor-approved fallback fixture, not from a
live Bloomberg connection. The output follows the canonical MarketPulse row
contract, so analytics.py is reused unchanged.
"""

import json
from pathlib import Path


ACCESS_MODE = "APPROVED_SAMPLE"
SAMPLE_PATH = Path("data/sample/bloomberg_reference_sample.json")

# MarketPulse canonical ticker -> Bloomberg identifier
BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}


def fetch_raw_bloomberg_history(identifier, sample_path=SAMPLE_PATH):
    """Raw input boundary: return the approved sample series for identifier."""
    with open(sample_path, encoding="utf-8") as file:
        sample = json.load(file)

    for series in sample["series"]:
        if series["provider_identifier"] == identifier:
            return series

    raise ValueError(f"No approved Bloomberg-stage series for {identifier}")


def normalize_bloomberg_history(raw_data, canonical_ticker):
    """Normalization boundary: teaching wrapper keys -> canonical rows."""
    if raw_data["canonical_ticker"] != canonical_ticker:
        raise ValueError(
            f"Series is {raw_data['canonical_ticker']}, "
            f"expected {canonical_ticker}"
        )

    return [
        {
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        }
        for observation in raw_data["observations"]
    ]


def fetch_bloomberg_prices(canonical_ticker):
    identifier = BLOOMBERG_IDENTIFIERS[canonical_ticker]
    raw_data = fetch_raw_bloomberg_history(identifier)
    rows = normalize_bloomberg_history(raw_data, canonical_ticker)

    if not rows:
        raise ValueError(f"No Bloomberg-stage rows for {identifier}")

    return rows
