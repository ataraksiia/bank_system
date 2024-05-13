from datetime import datetime

import pytest

from src.decorators import log


@pytest.fixture
def file_write_error() -> str:
    return f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} divide error: TypeError. Inputs: (2, '7'), {{}}"


@log("test.txt")
def divide(a: float | int, b: float | int) -> float:
    return a / b


def test_log_error(file_write_error: str) -> None:
    divide(2, "7")
    with open("test.txt", "r", encoding="utf-8") as file:
        last_str = file.readlines()[-1].strip()
    assert file_write_error == last_str


@pytest.fixture
def file_write() -> str:
    return f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} divide ok"


def test_log(file_write: str) -> None:
    divide(2, 7)
    with open("test.txt", "r", encoding="utf-8") as file:
        last_str = file.readlines()[-1].strip()
    assert file_write == last_str
