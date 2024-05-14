from typing import Iterator


def filter_by_currency(transaction_array: list, currency: str) -> Iterator:
    """Функция, которая принимает список словарей  и возвращает итератор, который по очеред выдает операции,
    в которых указана заданная валюта."""

    # Итерируемся по полученному списку и сравниваем валюты. Если одинаковые, то возвращаем итератор.
    for operation in transaction_array:
        if operation["operationAmount"]["currency"]["code"] == currency:
            yield operation


def transaction_descriptions(transaction_array: list) -> Iterator:
    """Функция, которая принимает список словарей и возвращает описание каждой операции по очереди."""
    # Итерируемся по полученному списку и возвращаем итератор с описанием операций.
    for operation in transaction_array:
        yield operation["description"]


def card_number_generator(start: int, end: int) -> Iterator:
    """Функция, которая генерирует номера карт."""
    for num in range(start, end + 1):
        card_number = f"{num:016d}"
        yield card_number
