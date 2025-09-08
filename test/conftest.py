import pytest

@pytest.fixture
def card_number():
    return '1111222233334444'

@pytest.fixture
def account_number():
    return '12345678901234567890'


@pytest.fixture
def invalid_card_number():
    return ['', 'qqqqwwwweeeerrrr', '1234567890', '1111 2222 3333 4444', '!@#$%^&*()_+_)(*']


@pytest.fixture
def invalid_account_number():
    return ['', 'qqqqwwwweeeerrrr', '1234567890', '1111 2222 3333 4444', '!@#$%^&*()_+_)(*']