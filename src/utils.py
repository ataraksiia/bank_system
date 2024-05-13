import json
import os

import requests
from dotenv import load_dotenv


def get_financial_transactions(json_file: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с
    данными о финансовых транзакциях"""

    try:
        with open(json_file, "r", encoding="UTF-8") as file:
            parsed_file = list(json.load(file))
    except Exception:
        return []
    else:
        return parsed_file


load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_transaction_amounts(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях. Если транзакция была в
    USD или EUR, идет обращение к внешнему API для получения текущего курса и конвертации суммы операции в рубли."""
    path_currency = transaction["operationAmount"]["currency"]["code"]
    if path_currency == "USD" or path_currency == "EUR":
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{path_currency}"
        response = requests.get(url, headers={"apikey": API_KEY})
        response_data = response.json()
        current_exchange_rate = response_data["conversion_rates"]["RUB"]
        return float(transaction["operationAmount"]["amount"]) * float(current_exchange_rate)
    else:
        return float(transaction["operationAmount"]["amount"])
