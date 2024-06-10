from unittest.mock import Mock, patch

from pandas import DataFrame

from src.transactions import read_transactions_csv_file, read_transactions_xlsx_file


@patch("pandas.read_csv")
def test_read_transactions_csv_file(mock_reader: Mock) -> None:
    mock_reader.return_value = DataFrame(
        {
            "id": ["650703"],
            "state": ["EXECUTED"],
            "date": ["2023-09-05T11:30:32Z"],
            "amount": ["16210"],
            "currency_name": ["Sol"],
            "currency_code": ["PEN"],
            "to": ["Счет 39745660563456619397"],
            "from": ["Счет 58803664561298323391"],
            "description": ["Перевод организации"],
        }
    )
    assert read_transactions_csv_file("../csv_excel/transactions.csv") == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "to": "Счет 39745660563456619397",
            "from": "Счет 58803664561298323391",
            "description": "Перевод организации",
        }
    ]


@patch("pandas.read_xlsx")
def test_read_transactions_xlsx_file(mock_reader: Mock) -> None:
    mock_reader.return_value = DataFrame(
        {
            "id": ["650703"],
            "state": ["EXECUTED"],
            "date": ["2023-09-05T11:30:32Z"],
            "amount": ["16210"],
            "currency_name": ["Sol"],
            "currency_code": ["PEN"],
            "to": ["Счет 39745660563456619397"],
            "from": ["Счет 58803664561298323391"],
            "description": ["Перевод организации"],
        }
    )
    assert read_transactions_xlsx_file("../csv_excel/transactions.csv") == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "to": "Счет 39745660563456619397",
            "from": "Счет 58803664561298323391",
            "description": "Перевод организации",
        }
    ]
