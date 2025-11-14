from unittest.mock import patch

from src.utils import transaction_amount


def test_transaction_amount_rub_only():
    """Тест когда все транзакции в рублях"""
    mock_transactions = [
        {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "500", "currency": {"code": "RUB"}}},
    ]

    with patch("src.utils.get_transaction_list", return_value=mock_transactions):
        result = transaction_amount("test.json")
        assert result == 1500.0


def test_transaction_amount_foreign_currency():
    """Тест когда транзакции в иностранной валюте"""
    mock_transactions = [{"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}]

    with patch("src.utils.get_transaction_list", return_value=mock_transactions):
        with patch("src.external_api.external_api_exchange", return_value=90.0):
            result = transaction_amount("test.json")
            assert result == 90.0


def test_transaction_amount_mixed_currencies():
    """Тест смешанных валют"""
    mock_transactions = [
        {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
        {"operationAmount": {"amount": "500", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "200", "currency": {"code": "EUR"}}},
    ]

    with patch("src.utils.get_transaction_list", return_value=mock_transactions):
        with patch("src.external_api.external_api_exchange") as mock_exchange:
            mock_exchange.side_effect = [90.0, 180.0]  # USD и EUR конвертация
            result = transaction_amount("test.json")
            # 90.0 (USD) + 500.0 (RUB) + 180.0 (EUR) = 770.0
            assert result == 770.0


def test_transaction_amount_empty_list():
    """Тест пустого списка транзакций"""
    mock_transactions = []

    with patch("src.utils.get_transaction_list", return_value=mock_transactions):
        result = transaction_amount("test.json")
        assert result == 0.0


def test_transaction_amount_missing_fields():
    """Тест с отсутствующими полями в транзакции"""
    mock_transactions = [{"operationAmount": {"amount": "100"}}]  # отсутствует currency

    with patch("src.utils.get_transaction_list", return_value=mock_transactions):
        result = transaction_amount("test.json")
        assert isinstance(result, str)  # Должен вернуть строку с ошибкой
        assert "Произошла ошибка" in result


def test_transaction_amount_conversion_error():
    """Тест ошибки конвертации валюты"""
    mock_transactions = [{"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}]

    with patch("src.utils.get_transaction_list", return_value=mock_transactions):
        with patch("src.external_api.external_api_exchange") as mock_exchange:
            mock_exchange.side_effect = ValueError("Invalid amount")
            result = transaction_amount("test.json")
            assert isinstance(result, str)
            assert "Ошибка конвертации" in result


def test_transaction_amount_conversion_exception():
    """Тест исключения при конвертации валюты"""
    mock_transactions = [{"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}]

    with patch("src.utils.get_transaction_list", return_value=mock_transactions):
        with patch("src.external_api.external_api_exchange") as mock_exchange:
            mock_exchange.side_effect = Exception("API connection failed")
            result = transaction_amount("test.json")
            assert isinstance(result, str)
            assert "Ошибка конвертации" in result


def test_transaction_amount_no_currency_code():
    """Тест без кода валюты"""
    mock_transactions = [{"operationAmount": {"amount": "100", "currency": {}}}]

    with patch("src.utils.get_transaction_list", return_value=mock_transactions):
        result = transaction_amount("test.json")
        assert isinstance(result, str)  # Должен вернуть строку с ошибкой
        assert "Произошла ошибка" in result
