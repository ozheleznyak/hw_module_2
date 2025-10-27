from unittest.mock import patch

import pytest

from src import utils


def test_transaction_amount_rub_only():
    """Тест когда все транзакции в рублях"""
    mock_transactions = [
        {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "500", "currency": {"code": "RUB"}}}
    ]

    with patch('src.utils.get_transaction_list', return_value=mock_transactions):
        with patch('src.external_api.external_api_exchange') as mock_exchange:
            mock_exchange.return_value = 0.0  # Не будет вызываться для RUB

            result = utils.transaction_amount("test.json")
            assert result == 1500.0


def test_transaction_amount_foreign_currency():
    """Тест когда есть транзакции в иностранной валюте"""
    mock_transactions = [
        {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "50", "currency": {"code": "USD"}}},
        {"operationAmount": {"amount": "200", "currency": {"code": "EUR"}}}
    ]

    with patch('src.utils.get_transaction_list', return_value=mock_transactions):
        with patch('src.external_api.external_api_exchange') as mock_exchange:
            # Мокаем возврат значений для разных валют
            mock_exchange.side_effect = [6500.0, 7200.0]  # USD и EUR в рублях

            result = utils.transaction_amount("test.json")
            assert result == 14700.0  # 1000 + 6500 + 7200


def test_transaction_amount_empty_list():
    """Тест пустого списка транзакций"""
    with patch('src.utils.get_transaction_list', return_value=[]):
        with patch('src.external_api.external_api_exchange') as mock_exchange:
            mock_exchange.return_value = 0.0

            result = utils.transaction_amount("test.json")
            assert result == 0.0


def test_transaction_amount_external_api_error():
    """Тест обработки ошибки внешнего API"""
    mock_transactions = [
        {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    ]

    with patch('src.utils.get_transaction_list', return_value=mock_transactions):
        with patch('src.external_api.external_api_exchange') as mock_exchange:
            mock_exchange.side_effect = Exception("API error")

            with pytest.raises(Exception):
                utils.transaction_amount("test.json")


def test_transaction_amount_zero_amount():
    """Тест нулевых сумм"""
    mock_transactions = [
        {"operationAmount": {"amount": "0", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "0", "currency": {"code": "USD"}}}
    ]

    with patch('src.utils.get_transaction_list', return_value=mock_transactions):
        with patch('src.external_api.external_api_exchange') as mock_exchange:
            mock_exchange.return_value = 0.0

            result = utils.transaction_amount("test.json")
            assert result == 0.0
