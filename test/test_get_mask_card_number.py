import pytest

from src.masks import get_mask_card_number


def test_valid_card_masks(card_number):
    assert get_mask_card_number(card_number) == '1111 22** **** 4444'


def test_invalid_card(invalid_card_number):
    with pytest.raises(ValueError):
        for arg in invalid_card_number:
            get_mask_card_number(arg)



