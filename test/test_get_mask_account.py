import pytest

from src.masks import get_mask_account


def test_valid_account_mask(account_number):
    assert get_mask_account(account_number) == '**7890'


def test_invalid_account(invalid_card_number):
    with pytest.raises(ValueError) as account_error_message:
        for account in invalid_card_number:
            get_mask_account(account)
    assert str(account_error_message.value) == 'You\'ve entered wrong account number. Please try again'
