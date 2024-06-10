from typing import Any

import pandas as pd


def read_transactions_csv_file(csv_file: str) -> list:
    """Считывание финансовые операций с CSV файла и возвращает список словарей"""
    reader = pd.read_csv(csv_file, delimiter=";")
    data = reader.to_dict(orient="records")
    return data


def read_transactions_xlsx_file(xlsx_file: str) -> Any:
    """Считывание финансовые операций с XLSX файла и возвращает DataFrame"""
    reader = pd.read_excel(xlsx_file)
    data = reader.to_dict(orient="records")
    return data


print(read_transactions_csv_file("../csv_excel/transactions.csv"))
print(read_transactions_xlsx_file("../csv_excel/transactions_excel.xlsx"))
