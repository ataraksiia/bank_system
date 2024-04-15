import pytest

from src.widget import card_or_account_data_mask, new_view_date


@pytest.mark.parametrize(
    "visible_data, mask_data",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic  6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum  8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold  5999 41** **** 6353"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_card_or_account_data_mask(visible_data: str, mask_data: str):
    assert card_or_account_data_mask(visible_data) == mask_data


@pytest.mark.parametrize(
    "date, mask_date",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
        ("2024-12-30T08:21:33.419441", "30.12.2024"),
        ("2015-3-1T08:21:33.018941", "1.3.2015"),
    ],
)
def test_new_view_date(date: str, mask_date: str):
    assert new_view_date(date) == mask_date
