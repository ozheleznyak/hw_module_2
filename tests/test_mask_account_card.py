import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "user_card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_different_valid_card_types(user_card, expected):
    assert mask_account_card(user_card) == expected


@pytest.mark.parametrize(
    "user_account, expected",
    [("Счет 73654108430135874305", "Счет **4305"), ("Account 73654108430135874305", "Account **4305")],
)
def test_different_valid_account_types(user_account, expected):
    assert mask_account_card(user_account) == expected


def test_card_numbers_only():
    with pytest.raises(IndexError):
        mask_account_card("73654108430135874305")


def test_account_numbers_only():
    with pytest.raises(IndexError):
        mask_account_card("11112222333344445555")


def test_no_spaces():
    with pytest.raises(ValueError):
        mask_account_card("Счет73654108430135874305")
    with pytest.raises(ValueError):
        mask_account_card("VisaPlatinum7000792289606361")


def test_wrong_account_number():
    with pytest.raises(ValueError):
        mask_account_card("Счет 736541084301358")


def test_wrong_card_number():
    with pytest.raises(ValueError):
        mask_account_card("Maestro 70007")


def test_card_number_special_characters():
    with pytest.raises(ValueError):
        mask_account_card("Maestro 1111^&*()_+_4444")


def test_account_number_special_characters():
    with pytest.raises(ValueError):
        mask_account_card('Счет 1234!"№%:,1234567890')
