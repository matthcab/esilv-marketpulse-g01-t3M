from pathlib import Path
import csv
import json
from providers.bloomberg_provider import load_sample_series, normalize_bloomberg_history
from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)

DATA_DIR = Path(__file__).resolve().parents[1] / "data/sample"

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"
PROVIDER_LABEL = "Bloomberg stage (APPROVED_SAMPLE)"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def normalize_price_row(row):
    return {
        "date": row["date"],
        "ticker": row["ticker"],
        "open": float(row["open"]),
        "high": float(row["high"]),
        "low": float(row["low"]),
        "close": float(row["close"]),
        "volume": int(row["volume"]),
    }


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return [normalize_price_row(row) for row in csv.DictReader(file)]


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]

def get_first_close(prices):
    first_row = prices[0]
    return float(first_row["close"])


def get_last_close(prices):
    last_row = prices[-1]
    return float(last_row["close"])

def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]

def display_market_summary(asset, prices, show_currency=True):
    first_close = get_first_close(prices)
    last_close = get_last_close(prices)

    if show_currency:
        unit = " " + asset["currency"]
    else:
        unit = ""

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Market       : {asset['market']}")
    print(f"Currency     : {asset['currency']}")
    print(f"Observations : {len(prices)}")
    print(f"First date   : {get_first_date(prices)}")
    print(f"Last date    : {get_last_date(prices)}")
    print(f"First close  : {first_close:.2f}{unit}")
    print(f"Last close   : {last_close:.2f}{unit}")


def build_market_snapshot():
    instruments = load_instruments()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    prices_by_ticker = {}
    for series in load_sample_series():
        ticker = series["canonical_ticker"]
        prices_by_ticker[ticker] = normalize_bloomberg_history(series)

    instrument_prices = prices_by_ticker[instrument["ticker"]]
    benchmark_prices = prices_by_ticker[benchmark["ticker"]]

    instrument_prices, benchmark_prices = align_series(
        instrument_prices,
        benchmark_prices,
    )
    if not instrument_prices:
        return None

    instrument_return = calculate_period_return(instrument_prices)
    benchmark_return = calculate_period_return(benchmark_prices)

    relative_performance = calculate_relative_performance(
        instrument_return,
        benchmark_return,
    )
    return {
        "provider": PROVIDER_LABEL,
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_prices": instrument_prices,
        "benchmark_prices": benchmark_prices,
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": relative_performance,
        "instrument_base_100": calculate_base_100(instrument_prices),
        "benchmark_base_100": calculate_base_100(benchmark_prices),
    }


def main():
    snapshot = build_market_snapshot()
    if snapshot is None:
        print("No common dates for the instrument and benchmark.")
        return

    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]
    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print(f"Period   : {snapshot['lookback']}")
    print(f"Interval : {snapshot['interval']}")
    print(f"Provider : {snapshot['provider']}")
    print()
    print("Instrument")
    display_market_summary(instrument, snapshot["instrument_prices"])
    print()
    print("Benchmark index")
    display_market_summary(benchmark, snapshot["benchmark_prices"], show_currency=False)

    print()
    print("Period returns")
    print(f"{instrument['ticker']} : {snapshot['instrument_return']:+.2f}%")
    print(f"{benchmark['ticker']} : {snapshot['benchmark_return']:+.2f}%")

    print()
    print("Relative performance")
    print(f"{snapshot['relative_performance']:+.2f} percentage points")

    instrument_base_100 = snapshot["instrument_base_100"]
    benchmark_base_100 = snapshot["benchmark_base_100"]

    print()
    print("Base 100")

    print(
        f"{instrument['ticker']} : "
        f"{instrument_base_100[0]['value']:.2f} -> "
        f"{instrument_base_100[-1]['value']:.2f}"
    )

    print(
        f"{benchmark['ticker']} : "
        f"{benchmark_base_100[0]['value']:.2f} -> "
        f"{benchmark_base_100[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()
