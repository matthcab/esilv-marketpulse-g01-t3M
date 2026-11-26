import json
from pathlib import Path


BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}

SAMPLE_PATH = Path("data/sample/bloomberg_reference_sample.json")


def load_bloomberg_sample(identifier):
    with open(SAMPLE_PATH, encoding="utf-8") as file:
        data = json.load(file)

    for series in data["series"]:
        if series["provider_identifier"] == identifier:
            return series

    raise ValueError(
        f"No approved sample found for {identifier}"
    )

def normalize_bloomberg_history(raw_data, canonical_ticker):
    rows = []

    for observation in raw_data:
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

    series = load_bloomberg_sample(identifier)

    return normalize_bloomberg_history(
        series["observations"],
        series["canonical_ticker"],
    )


if __name__ == "__main__":
    instrument_prices = fetch_bloomberg_prices("AAPL")
    benchmark_prices = fetch_bloomberg_prices("SP500")

    print("AAPL :", len(instrument_prices), "observations")
    print(instrument_prices[0])

    print("SP500 :", len(benchmark_prices), "observations")
    print(benchmark_prices[0])

    expected_path = Path(
        "data/sample/bloomberg_reference_expected.json"
    )

    with open(expected_path, encoding="utf-8") as file:
        expected = json.load(file)

    normalized_rows = instrument_prices + benchmark_prices

    print(
        "Résultat conforme à la référence :",
        normalized_rows == expected["rows"],
    )