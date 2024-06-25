import os.path

from src.processing import filter_by_str, filter_list_by_date, filter_list_by_state
from src.transactions import read_transactions_csv_file, read_transactions_xlsx_file
from src.utils import get_financial_transactions
from src.widget import card_or_account_data_mask, new_view_date


def select_the_file_format() -> list:
    user_input = input(
        """Привет! Добро пожаловать в программу работы с банковскими транзакициями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из json файла
    2. Получить информацию о транзакциях из csv файла
    3. Получить информацию о транзакциях из xlsx файла\n"""
    )
    if user_input == "1":
        print("Для обработки выбран json файл")
        return get_financial_transactions(os.path.join("..", "data", "operations.json"))

    elif user_input == "2":
        print("Для обработки выбран csv файл")
        return read_transactions_csv_file(os.path.join("..", "csv_excel", "transactions.csv"))

    print("Для обработки выбран xlsx файл")
    return read_transactions_xlsx_file(os.path.join("..", "csv_excel", "transactions_excel.xlsx"))


def select_of_operation_status(data: list[dict]) -> list[dict]:
    user_input = input("""Введите статус по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""")
    while user_input.upper() != "EXECUTED" or user_input.upper() != "CANCELED" or user_input.upper() != "PENDING":
        if user_input.upper() == "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
            return filter_list_by_state(data, user_input.upper())

        elif user_input.upper() == "CANCELED":
            print('Операции отфильтрованы по статусу "CANCELED"')
            return filter_list_by_state(data, user_input.upper())
        elif user_input.upper() == "PENDING":
            print('Операции отфильтрованы по статусу "PENDING"')
            return filter_list_by_state(data, user_input.upper())

        else:
            print(
                f"Статус операции {user_input} недоступен. "
                f"Введите статус по которому необходимо выполнить фильтрацию. "
                f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            )
            user_input = input()
    return data


def operation_output_format(data: list[dict]) -> list[dict]:
    sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if sort_by_date == "да":
        sort_by_value = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        if "возр" in sort_by_value:
            return filter_list_by_date(data, False)
        else:
            return filter_list_by_date(data)
    return data


def operation_output_format_2(data: list[dict]) -> list[dict]:
    sort_by_currency = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
    new_data = []
    if sort_by_currency == "да":
        for object in data:
            for k in object.keys():
                if k == "operationAmount":
                    if object["operationAmount"]["currency"]["code"] == "RUB":
                        new_data.append(object)
                elif k == "currency_code":
                    if object["currency_code"] == "RUB":
                        new_data.append(object)
        return new_data
    return data


def operation_output_format_3(data: list[dict]) -> list[dict]:
    sort_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    if sort_by_word == "да":
        print("Введите слово")
        user_input = input().lower()
        return filter_by_str(data, user_input)
    return data


def output(data: list[dict]) -> None:
    is_json = False
    for object in data:
        if "operationAmount" in object.keys():
            is_json = True
            break
        elif "currency_code" in object.keys():
            is_json = False
            break
    if is_json:
        for transaction in data:
            if "Перевод" in transaction.get("description", ""):
                print(
                    f"{new_view_date(transaction['date'])} {transaction['description']}\n"
                    f"{card_or_account_data_mask((transaction['from']))} -> "
                    f"{card_or_account_data_mask((transaction['to']))}\n"
                    f"Сумма: {transaction['operationAmount']['amount']} "
                    f"{transaction['operationAmount']['currency']['name']}\n"
                )
            else:
                print(
                    f"{new_view_date(transaction['date'])} {transaction['description']}\n"
                    f"{card_or_account_data_mask((transaction['to']))}\n"
                    f"Сумма: {transaction['operationAmount']['amount']} "
                    f"{transaction['operationAmount']['currency']['name']}\n"
                )
    else:
        for transaction in data:
            if "Перевод" in transaction.get("description", ""):
                print(
                    f"{new_view_date(transaction['date'])} {transaction['description']}\n"
                    f"{card_or_account_data_mask((transaction['from']))} -> "
                    f"{card_or_account_data_mask((transaction['to']))}\n"
                    f"Сумма: {transaction['amount']} {transaction['currency_name']}\n"
                )
            else:
                print(
                    f"{new_view_date(transaction['date'])} {transaction['description']}\n"
                    f"{card_or_account_data_mask((transaction['to']))}\n"
                    f"Сумма: {transaction['amount']} {transaction['currency_name']}\n"
                )


if __name__ == "__main__":
    data = select_the_file_format()
    data = select_of_operation_status(data)
    data = operation_output_format(data)
    data = operation_output_format_2(data)
    data = operation_output_format_3(data)
    print("Распечатываю итоговый список транзакций...\n")
    count = 0
    for i in data:
        count += 1
    print(f"Всего банковских операций в выборке: {count}\n")
    output(data)
