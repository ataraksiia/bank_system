from src.logger import setup_logger

logger = setup_logger("masks", "masks.log")


def card_number_mask(card_number: str) -> str:
    """Функция, которая возвращает маскированный номер карты"""

    # Делаем строку списком и записываем в новую переменную
    card_number_list = list(card_number)

    # C помощью среза заменяем символы на *
    card_number_list[6:12] = ["*", "*", "*", "*", "*", "*"]
    logger.info(f"start card_number_mask {card_number}")
    # Выводим результат с помощью распаковки списка срезами
    result = (
        f'{"".join(card_number_list[0:4])} {"".join(card_number_list[4:8])} '
        f'{"".join(card_number_list[8:12])} {"".join(card_number_list[12:])}'
    )
    logger.info(f"mask {result}")
    return result


card_number_mask("0123456789111111")


def account_number_mask(account_number: str) -> str:
    """Функция, которая возвращает маскированный номер cчёта"""

    logger.info(f"start account_number_mask {account_number}")

    # Выводим результат с помощью среза cтроки
    result = f"**{account_number[-4:]}"
    logger.info(f"mask {result}")
    return result


account_number_mask("73654108430135874305")
