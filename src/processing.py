import re
from collections import Counter


def filter_list_by_state(received_list: list, state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает на вход список словарей и значение для ключа state
    и возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение"""

    # Разбиваем переданный итерируемый объект на элементы и передаем каждый их них в функцию
    # Если в словаре списка значение ключа state совпадает с нужным нам, то добавляем словарь в новый список
    final_list = list(filter(lambda x: x.get("state", "") == state, received_list))

    return final_list


def filter_list_by_date(received_list: list, reverse: bool = True) -> list:
    """Функция, которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию/возрастанию даты"""

    # Сортируем список по значению даты
    final_list = sorted(received_list, key=lambda x: x.get("date", "1"), reverse=reverse)

    return final_list


def filter_by_str(transactions: list, line: str) -> list[dict]:
    """Возвращет список словарей у которых в описании есть данная строка"""
    data = []
    for transaction in transactions:
        if re.search(line.lower(), transaction.get("description", "").lower()):
            data.append(transaction)
    return data


def filter_by_category(transactions: list, category_list: list) -> Counter:
    """Возвращает словарь, в котором ключи - названия категорий, а значения - количество операций в каждой категории"""
    new_list = []
    for transaction in transactions:
        if transaction.get("description") in category_list:
            new_list.append(transaction.get("description"))
    counted = Counter(new_list)
    return counted
