import yfinance as yf


YAHOO_SYMBOLS = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(ticker, period="1mo", interval="1d"):
    symbol = YAHOO_SYMBOLS[ticker]
    history = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False,
    )

    if history.empty:
        raise ValueError(f"Yahoo Finance n'a renvoyé aucun prix pour {symbol}")

    prices = []
    for date, row in history.iterrows():
        prices.append({
            "date": date.strftime("%Y-%m-%d"),
            "ticker": ticker,
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        })

    return prices


if __name__ == "__main__":
    for ticker in ("AAPL", "SP500"):
        prices = fetch_yahoo_prices(ticker)
        print(prices[0])