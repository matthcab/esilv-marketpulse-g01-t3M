import json
from pathlib import Path


ACCESS_MODE = "APPROVED_SAMPLE"
SAMPLE_PATH = Path("data/sample/bloomberg_reference_sample.json")

BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}


def load_approved_sample(path=SAMPLE_PATH):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def find_series(raw_data, identifier):
    for series in raw_data["series"]:
        if series["provider_identifier"] == identifier:
            return series

    raise ValueError(f"No approved Bloomberg sample series for {identifier}")


def normalize_bloomberg_history(series, canonical_ticker):
    if series["canonical_ticker"] != canonical_ticker:
        raise ValueError(
            f"Sample series is {series['canonical_ticker']}, expected {canonical_ticker}"
        )

    rows = []

    for observation in series["observations"]:
        rows.append({
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })

    return rows


def fetch_bloomberg_prices(canonical_ticker):
    identifier = BLOOMBERG_IDENTIFIERS[canonical_ticker]
    raw_data = load_approved_sample()
    series = find_series(raw_data, identifier)

    rows = normalize_bloomberg_history(series, canonical_ticker)

    if not rows:
        raise ValueError(f"No Bloomberg-stage rows for {identifier}")

    return rows