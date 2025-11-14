from unittest.mock import mock_open, patch

import pandas as pd

from src.transactions_from_csv import get_transactions_from_csv


def test_get_transactions_from_csv_success():
    """тест успешного выполнения"""

    mock_data = pd.DataFrame(
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
                "to": "9012",
            }
        ]
    )

    # Мокаем pandas.read_csv
    with patch("pandas.read_csv", return_value=mock_data):
        # Мокаем open для записи JSON
        with patch("builtins.open", mock_open()) as mocked_file:
            result = get_transactions_from_csv("test.csv")

            assert result == [
                {
                    "id": 1,
                    "state": "EXECUTED",
                    "date": "2023-01-01",
                    "operationAmount": {"amount": "100.0", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Payment 1",
                    "from": "1234",
                    "to": "9012",
                }
            ]

            mocked_file.assert_called_once()


def test_get_transactions_from_csv_empty_data():
    """Тест с пустыми данными"""

    # Мокаем пустой DataFrame
    mock_empty_data = pd.DataFrame()

    with patch("pandas.read_csv", return_value=mock_empty_data):
        with patch("builtins.open", mock_open()):
            result = get_transactions_from_csv("empty.csv")

            # Проверяем, что вернулся пустой список
            assert result == []


def test_get_transactions_from_csv_with_nan_values():
    """Тест с NaN значениями"""

    mock_data = pd.DataFrame(
        [
            {
                "id": None,
                "state": None,
                "date": None,
                "amount": None,
                "currency_name": None,
                "currency_code": None,
                "description": None,
                "from": "",
                "to": None,
            }
        ]
    )

    with patch("pandas.read_csv", return_value=mock_data):
        with patch("builtins.open", mock_open()):
            result = get_transactions_from_csv("test.csv")

            # Проверяем, что NaN заменены на пустые строки
            assert result == [
                {
                    "id": None,
                    "state": "",
                    "date": "",
                    "operationAmount": {"amount": "", "currency": {"name": "", "code": ""}},
                    "description": "",
                    "from": "",
                    "to": "",
                }
            ]
