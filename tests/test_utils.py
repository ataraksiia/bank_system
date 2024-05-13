import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.utils import get_financial_transactions, get_transaction_amounts


@pytest.mark.parametrize(
    "json_file, parsed_file",
    [
        ("data/does_not_exist_file.json", []),
        ("check_for_test.json", []),
        ("data/operations.json", get_financial_transactions("data/operations.json")),
    ],
)
def test_get_financial_transactions(json_file: str, parsed_file: list) -> None:
    assert get_financial_transactions(json_file) == parsed_file


load_dotenv()
API_KEY = os.getenv("API_KEY")


@patch("requests.get")
def test_get_transaction_amounts_EUR(mock_get):
    mock_get.return_value.json.return_value = {
        "result": "success",
        "documentation": "https://www.exchangerate-api.com/docs",
        "terms_of_use": "https://www.exchangerate-api.com/terms",
        "time_last_update_unix": 1715558401,
        "time_last_update_utc": "Mon, 13 May 2024 00:00:01 +0000",
        "time_next_update_unix": 1715644801,
        "time_next_update_utc": "Tue, 14 May 2024 00:00:01 +0000",
        "base_code": "EUR",
        "conversion_rates": {"RUB": 98},
    }
    assert (
            get_transaction_amounts(
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                }
            )
            == 805694.2600000001
    )
    mock_get.assert_called_once_with(
        f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/EUR", headers={"apikey": API_KEY}
    )


@patch("requests.get")
def test_get_transaction_amounts_USD(mock_get):
    mock_get.return_value.json.return_value = {
        "result": "success",
        "documentation": "https://www.exchangerate-api.com/docs",
        "terms_of_use": "https://www.exchangerate-api.com/terms",
        "time_last_update_unix": 1715558401,
        "time_last_update_utc": "Mon, 13 May 2024 00:00:01 +0000",
        "time_next_update_unix": 1715644801,
        "time_next_update_utc": "Tue, 14 May 2024 00:00:01 +0000",
        "base_code": "USD",
        "conversion_rates": {"RUB": 98},
    }
    assert (
            get_transaction_amounts(
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                }
            )
            == 805694.2600000001
    )
    mock_get.assert_called_once_with(
        f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD", headers={"apikey": API_KEY}
    )


@patch("requests.get")
def test_get_transaction_amounts_RUB(mock_get):
    assert (
            get_transaction_amounts(
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                }
            )
            == 8221.37
    )
