import pytest

from src.masks import account_number_mask, card_number_mask


@pytest.fixture
def accounts() -> list:
    return ["73654108430135874305", "64686473678894779589", "11113333430135873020", "09854108430135875647"]


@pytest.fixture
def cards() -> list:
    return ["7000792289606361", "1596837868705199", "8990922113665229"]


def test_account_number_mask(accounts: str) -> None:
    examination = []
    for account in accounts:
        examination.append(account_number_mask(account))
    assert examination == ["**4305", "**9589", "**3020", "**5647"]


def test_card_number_mask(cards: str) -> None:
    examination = []
    for card in cards:
        examination.append(card_number_mask(card))
    assert examination == ["7000 79** **** 6361", "1596 83** **** 5199", "8990 92** **** 5229"]
