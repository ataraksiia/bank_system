from src.masks import account_number_mask, card_number_mask


def card_or_account_data_mask(visible_data: str) -> str:
    """Функция, которая возвращает информацию и маскированный номер карты или счета"""

    # Проверяем, являются ли первые соединенные четыре символа словом "Счет".
    # Если да, то вызываем функцию account_number_mask из masks.py для маскировки номера счета
    if "Счет" in visible_data:
        return f"Счет {account_number_mask(visible_data)}"

    else:
        # В ином случае строка является картой
        # Разделяем полученные данные по пробелу и заносим в список
        card_data_and_number = visible_data.split(" ")

        # В новый список кладем элемент с -1 индексом, так как он всегда будет являться номером карты
        card_number = "".join(card_data_and_number[-1])

        # Проверяем кол-во элементов в первом списке, в который изначально была положена строка visible_data
        # Если элементов 3, то это значит, что наименование карты состоит из двух слов
        # Возвращаем данные, используя срез списка visible_data[0:2] - это наименование карты из двух слов
        # и с помощью функции card_number из masks.py маскируем данные карты
        if len(card_data_and_number) == 3:
            return f'{" ".join(card_data_and_number[0:2])}  {card_number_mask(card_number)}'

        # В ином случае возвращаем данные из списка visible_data используя индекс [0] - это наименование карты
        # и с помощью функции card_number из masks.py маскируем данные карты

        return f'{"".join(card_data_and_number[0])} ' f"{card_number_mask(card_number)}"


def new_view_date(date: str) -> str:
    """Функция, которая возвращает дату"""

    # Разделаем полученную строку с помощью split
    view_date = date.split("-")

    # В новый список добавляем элемент с индексом 3,
    # где число месяца сливается с буквами
    date_number = view_date[2]

    # Разделаем элемент с помощью split
    date_number.split(":")

    # Создаём новый список для числа
    date = ""

    # Начинаем итерацию по элементу,
    # где число нельзя отделить с помощью split(":").
    # В такой строке может быть не только двузначное число, но и однозначное,
    # поэтому проверяем является ли  символ цифрой,
    # если да - то добавляем цифру в список, иначе прерываем цикл
    for symbol in date_number:
        if symbol.isdigit():
            date += symbol
        else:
            break

    # Возвращаем число месяца из списка date,
    # а год месяц из списка view_date
    return f"{date}.{view_date[1]}.{view_date[0]}"
