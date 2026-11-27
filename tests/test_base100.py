import pytest

from src.analytics import calculate_base_100


def test_calculate_base_100():
    prices = [
        {"date": "2026-09-01", "ticker": "AAPL", "close": 250.0},
        {"date": "2026-09-02", "ticker": "AAPL", "close": 275.0},
    ]

    result = calculate_base_100(prices)

    assert len(result) == 2
    assert result[0]["value"] == pytest.approx(100.0)
    assert result[1]["value"] == pytest.approx(110.0)
    