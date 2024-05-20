import json
import os

import requests
from dotenv import load_dotenv

from src.logger import setup_logger

logger = setup_logger("utils", "utils.log")


def get_financial_transactions(json_file: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с
    данными о финансовых транзакциях"""
    logger.info(f"start get_financial_transactions {json_file}")
    try:
        with open(json_file, "r", encoding="UTF-8") as file:
            parsed_file = list(json.load(file))
    except Exception:
        logger.info("transactions []")
        return []
    else:
        logger.info(f"transactions {parsed_file}")
        return parsed_file


get_financial_transactions("../data/operations.json")

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_transaction_amounts(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях. Если транзакция была в
    USD или EUR, идет обращение к внешнему API для получения текущего курса и конвертации суммы операции в рубли."""
    logger.info(f"start get_transaction_amounts {transaction}")
    path_currency = transaction["operationAmount"]["currency"]["code"]
    if path_currency == "USD" or path_currency == "EUR":
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{path_currency}"
        response = requests.get(url, headers={"apikey": API_KEY})
        response_data = response.json()
        current_exchange_rate = response_data["conversion_rates"]["RUB"]
        result = float(transaction["operationAmount"]["amount"]) * float(current_exchange_rate)
        logger.info(f"sum {result}")
        return result
    else:
        result = float(transaction["operationAmount"]["amount"])
        logger.info(f"sum {result}")
        return result


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
