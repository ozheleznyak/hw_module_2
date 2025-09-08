import pytest

@pytest.fixture
def card_number():
    return '1111222233334444'

@pytest.fixture
def account_number():
    return '12345678901234567890'