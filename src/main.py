from pathlib import Path
import csv
import json

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"
PROVIDER_LABEL = "CSV"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]

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


def main():
    instruments = load_instruments()
    raw_prices = load_prices()
    prices = [normalize_price_row(row) for row in raw_prices]
    
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)
    relative_performance = calculate_relative_performance(
        instrument_return,
        benchmark_return,
    )

    instrument_base_100 = calculate_base_100(aligned_instrument)
    benchmark_base_100 = calculate_base_100(aligned_benchmark)

    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print(f"Period   : {LOOKBACK_LABEL}")
    print(f"Interval : {INTERVAL_LABEL}")
    print(f"Provider : {PROVIDER_LABEL}")
    print()
    print("Instrument")
    display_market_summary(instrument, instrument_prices)
    print(f"Period return : {instrument_return:.2f}%")
    print()
    print("Benchmark index")
    display_market_summary(benchmark, benchmark_prices, show_currency=False)
    print(f"Period return : {benchmark_return:.2f}%")
    print()
    print("Relative performance")
    print(
        f"{instrument['ticker']} vs {benchmark['ticker']} : "
        f"{relative_performance:+.2f} percentage points"
    )
    print()
    print("Base 100")
    print(
        f"{instrument['ticker']:<6}: "
        f"{instrument_base_100[0]['value']:.2f} -> "
        f"{instrument_base_100[-1]['value']:.2f}"
    )
    print(
        f"{benchmark['ticker']:<6}: "
        f"{benchmark_base_100[0]['value']:.2f} -> "
        f"{benchmark_base_100[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()
