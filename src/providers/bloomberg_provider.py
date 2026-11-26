import json
from pathlib import Path


SAMPLE_FILE = Path(__file__).resolve().parents[2] / "data/sample/bloomberg_reference_sample.json"

BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}


def load_sample_series():
    with SAMPLE_FILE.open(encoding="utf-8") as file:
        data = json.load(file)
    return data["series"]

def normalize_bloomberg_history(series):
    ticker = series["canonical_ticker"]
    if series["provider_identifier"] != BLOOMBERG_IDENTIFIERS[ticker]:
        raise ValueError(f"Identifiant Bloomberg incohérent pour {ticker}")

    rows = []
    for observation in series["observations"]:
        rows.append({
            "date": observation["observation_date"],
            "ticker": ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })
    return rows

if __name__ == "__main__":
    
    for series in load_sample_series():
        ticker = series["canonical_ticker"]
        identifier = series["provider_identifier"]
        count = len(series["observations"])
        print(f"{ticker} | {identifier} | {count} observations")