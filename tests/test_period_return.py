import pytest

from analytics import calculate_period_return


@pytest.fixture
def prices():
    return [
        {"date": "2026-09-01", "ticker": "AAPL", "close": 250.0},
        {"date": "2026-09-02", "ticker": "AAPL", "close": 255.0},
        {"date": "2026-09-30", "ticker": "AAPL", "close": 266.2},
    ]


def test_period_return_known_value(prices):
    assert calculate_period_return(prices) == pytest.approx(6.48)
