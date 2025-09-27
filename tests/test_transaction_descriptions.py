import pytest

from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    "expected1, expected2, expected3, expected4, expected5",
    [
        (
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        )
    ],
)
def test_normal_usage_transaction_descriptions(
    test_transactions, expected1, expected2, expected3, expected4, expected5
):
    """проверяем типовое использование генератора"""
    generator = transaction_descriptions(test_transactions)
    assert next(generator) == expected1
    assert next(generator) == expected2
    assert next(generator) == expected3
    assert next(generator) == expected4
    assert next(generator) == expected5


def test_no_description_transaction_descriptions(test_transactions_no_description):
    """проверяем корректность обработки отсутствующего поля с описанием хотя бы в одной транзакции"""
    generator = transaction_descriptions(test_transactions_no_description)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "<No description for this transaction>"
    assert next(generator) == "Перевод со счета на счет"


def test_no_descriptions_transaction_descriptions(test_transactions_no_descriptions):
    """проверяем корректность обработки отсутствующего поля с описанием в принципе"""
    generator = transaction_descriptions(test_transactions_no_descriptions)
    assert next(generator) == "<No description for this transaction>"
    assert next(generator) == "<No description for this transaction>"


def test_empty_list_transaction_descriptions():
    """проверяем корректность обработки пустого списка"""
    generator = transaction_descriptions([])
    assert next(generator) == "Transaction list is empty"
