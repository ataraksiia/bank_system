def card_number_mask(card_number: str) -> str:
    """Функция, которая возвращает маскированный номер карты"""

    # Делаем строку списком и записываем в новую переменную
    card_number_list = list(card_number)

    # C помощью среза заменяем символы на *
    card_number_list[6:12] = ["*", "*", "*", "*", "*", "*"]

    # Выводим результат с помощью распаковки списка срезами
    return (
        f'{"".join(card_number_list[0:4])} {"".join(card_number_list[4:8])} '
        f'{"".join(card_number_list[8:12])} {"".join(card_number_list[12:])}'
    )


def account_number_mask(account_number: str) -> str:
    """Функция, которая возвращает маскированный номер cчёта"""

    # Выводим результат с помощью среза cтроки
    return f"**{account_number[-4:]}"
