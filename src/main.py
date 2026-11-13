from pathlib import Path
import csv
import json


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def main():
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    instrument_latest = instrument_prices[-1]
    benchmark_latest = benchmark_prices[-1]
    instrument_first_date = get_first_date(instrument_prices)
    instrument_last_date = get_last_date(instrument_prices)
    benchmark_first_date = get_first_date(benchmark_prices)
    benchmark_last_date = get_last_date(benchmark_prices)

    print("=== MarketPulse ===")
    print()
    print("Instrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Observations : {len(instrument_prices)}")
    print(f"First date   : {instrument_first_date}")
    print(f"Last date    : {instrument_last_date}")
    print(f"First close  : {instrument_prices[0]['close']} {instrument['currency']}")
    print(f"Last close   : {instrument_latest['close']} {instrument['currency']}")
    print()
    print("Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Observations : {len(benchmark_prices)}")
    print(f"First date   : {benchmark_first_date}")
    print(f"Last date    : {benchmark_last_date}")
    print(f"First close  : {benchmark_prices[0]['close']}")
    print(f"Last close   : {benchmark_latest['close']}")
    print()
    print(f"Period: {LOOKBACK_LABEL}")
    print(f"Interval: {INTERVAL_LABEL}")


if __name__ == "__main__":
    main()
