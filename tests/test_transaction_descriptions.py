import pytest

from data.transactions import test_transactions
from src.generators import transaction_descriptions

@pytest.mark.parametrize("expected1, expected2, expected3, expected4, expected5", [("Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации")])
def test_normal_usage_transaction_descriptions(test_transactions, expected1, expected2, expected3, expected4, expected5):
    """проверяем типовое использование генератора"""
    generator = transaction_descriptions(test_transactions)
    assert next(generator) == expected1
    assert next(generator) == expected2
    assert next(generator) == expected3
    assert next(generator) == expected4
    assert next(generator) == expected5


