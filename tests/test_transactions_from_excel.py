from unittest.mock import mock_open, patch

import pandas as pd

from src.transactions_from_excel import get_transactions_from_excel


def test_get_transactions_from_excel_success():
    """Тест успешного выполнения функции"""

    # Подготавливаем мок данных Excel
    mock_excel_data = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-01-01",
                "amount": 100.0,
                "currency_name": "USD",
                "currency_code": "USD",
                "description": "Payment 1",
                "from": "1234",
                "to": "5678",
            }
        ]
    )

    expected_result = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01",
            "operationAmount": {"amount": "100.0", "currency": {"name": "USD", "code": "USD"}},
            "description": "Payment 1",
            "from": "1234",
            "to": "5678",
        }
    ]

    with patch("pandas.read_excel", return_value=mock_excel_data):
        with patch("builtins.open", mock_open()):
            result = get_transactions_from_excel("/test/file.xlsx")

            assert result == expected_result


def test_get_transactions_from_excel_file_not_found():
    """Тест обработки ошибки отсутствия файла"""

    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        with patch("builtins.print") as mock_print:
            result = get_transactions_from_excel("/nonexistent/file.xlsx")

            assert result == []
            mock_print.assert_called()


def test_get_transactions_from_excel_empty_data():
    """Тест с пустыми данными"""

    mock_empty_data = pd.DataFrame()

    with patch("pandas.read_excel", return_value=mock_empty_data):
        with patch("builtins.open", mock_open()):
            result = get_transactions_from_excel("/test/file.xlsx")

            assert result == []


def test_get_transactions_from_excel_with_nan_values():
    """Тест с NaN значениями"""

    mock_excel_data = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-01-01",
                "amount": 100.0,
                "currency_name": "USD",
                "currency_code": "USD",
                "description": "Payment 1",
                "from": None,
                "to": None,
            }
        ]
    )

    with patch("pandas.read_excel", return_value=mock_excel_data):
        with patch("builtins.open", mock_open()):
            result = get_transactions_from_excel("/test/file.xlsx")

            assert len(result) == 1
            assert result[0]["from"] is None
            assert result[0]["to"] is None


def test_get_transactions_from_excel_json_write_error():
    """Тест ошибки записи JSON"""

    mock_excel_data = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-01-01",
                "amount": 100.0,
                "currency_name": "USD",
                "currency_code": "USD",
                "description": "Payment 1",
                "from": "1234",
                "to": "5678",
            }
        ]
    )

    with patch("pandas.read_excel", return_value=mock_excel_data):
        with patch("builtins.open", side_effect=PermissionError):
            with patch("builtins.print") as mock_print:
                result = get_transactions_from_excel("/test/file.xlsx")

                assert len(result) == 1  # Данные должны быть возвращены даже при ошибке записи
                mock_print.assert_called()


def test_get_transactions_from_excel_normal_case():
    """Тест обычного случая с нормальными данными"""

    mock_excel_data = pd.DataFrame(
        [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-01-01",
                "amount": 100.0,
                "currency_name": "USD",
                "currency_code": "USD",
                "description": "Payment 1",
                "from": "1234",
                "to": "5678",
            },
            {
                "id": 2,
                "state": "PENDING",
                "date": "2023-01-02",
                "amount": 200.0,
                "currency_name": "EUR",
                "currency_code": "EUR",
                "description": "Payment 2",
                "from": "9012",
                "to": "3456",
            },
        ]
    )

    with patch("pandas.read_excel", return_value=mock_excel_data):
        with patch("builtins.open", mock_open()):
            result = get_transactions_from_excel("/test/file.xlsx")

            assert len(result) == 2
            assert result[0]["id"] == 1
            assert result[1]["id"] == 2
            assert result[0]["operationAmount"]["currency"]["code"] == "USD"
            assert result[1]["operationAmount"]["currency"]["code"] == "EUR"
