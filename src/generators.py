from typing import Iterator


def filter_by_currency(transaction_array: list, currency: str) -> Iterator:
    """Функция, которая принимает список словарей  и возвращает итератор, который по очеред выдает операции,
    в которых указана заданная валюта."""

    # Итерируемся по полученному списку и сравниваем валюты. Если одиннаковые, то возвращаем итератор.
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
    card_numbers = "0000000000000000"
    # Нужно сгенерировать столько карт, сколько в end. В зависимости от величины числа в end, генерируем карты.
    for num in range(start, end + 1):
        if end < 10:
            generate_numbers = card_numbers[:-1] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 10 <= end < 100:
            generate_numbers = card_numbers[:-2] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 100 <= end <= 1000:
            generate_numbers = card_numbers[:-3] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 1_000 <= end < 10_000:
            generate_numbers = card_numbers[:-4] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 10_000 <= end < 100_000:
            generate_numbers = card_numbers[:-5] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 100_000 <= end < 1_000_000:
            generate_numbers = card_numbers[:-6] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 1_000_000 <= end < 10_000_000:
            generate_numbers = card_numbers[:-7] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 10_000_000 <= end < 100_000_000:
            generate_numbers = card_numbers[:-8] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 100_000_000 <= end < 1_000_000_000:
            generate_numbers = card_numbers[:-9] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 1_000_000_000 <= end < 10_000_000_000:
            generate_numbers = card_numbers[:-10] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 10_000_000_000 <= end < 100_000_000_000:
            generate_numbers = card_numbers[:-11] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 100_000_000_000 <= end < 1_000_000_000_000:
            generate_numbers = card_numbers[:-12] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 1_000_000_000_000 <= end < 10_000_000_000_000:
            generate_numbers = card_numbers[:-13] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 10_000_000_000_000 <= end < 100_000_000_000_000:
            generate_numbers = card_numbers[:-14] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 100_000_000_000_000 <= end < 1_000_000_000_000_000:
            generate_numbers = card_numbers[:-15] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
        elif 1_000_000_000_000_000 <= end < 10_000_000_000_000_000:
            generate_numbers = card_numbers[:-16] + str(num)
            yield (
                f'{"".join(generate_numbers[0:4])} {"".join(generate_numbers[4:8])} '
                f'{"".join(generate_numbers[8:12])} {"".join(generate_numbers[12:])}'
            )
