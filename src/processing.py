def sort_list_by_state(received_list: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает на вход список словарей и значение для ключа state
    и возвращает новый список, содержащий только те словари, у которых ключ state
    содержит переданное в функцию значение"""

    # Разбиваем переданный итерируемый объект на элементы и передаем каждый их них в функцию
    # Если в словаре списка значение ключа state совпадает с нужным нам, то добавляем словарь в новый список
    final_list = list(filter(lambda x: x["state"] == state, received_list))

    return final_list


def sort_list_by_date(received_list: list, reverse: bool = True) -> list:
    """Функция, которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию/возрастанию даты"""

    # Сортируем список по значению даты
    final_list = sorted(received_list, key=lambda x: x["date"], reverse=reverse)

    return final_list
