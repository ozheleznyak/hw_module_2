from unittest.mock import patch
from src import utils
import json
import pytest
import os


def test_get_transaction_list_success_with_mock_json_load():
    """Тест успешной работы функции"""
    file_path = "transactions.json"
    expected_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    with patch("os.path.abspath", return_value="/absolute/path/transactions.json"):
        with patch("builtins.open") as mock_open:
            with patch("json.load", return_value=expected_data):
                result = utils.get_transaction_list(file_path)
                assert result == expected_data
                mock_open.assert_called_once_with("/absolute/path/transactions.json", encoding="UTF-8")


def test_get_transaction_list_json_decode_error():
    """Тест обработки JSONDecodeError"""
    with patch("builtins.open") as mock_file:
        mock_file.side_effect = json.JSONDecodeError("Expecting value", "", 0)
        with patch("os.path.abspath", return_value="/test/path/file.json"):
            result = utils.get_transaction_list("/test/file.json")
            assert result == []


def test_get_transaction_list_file_not_found():
    """Тест обработки FileNotFoundError"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with patch("os.path.abspath", return_value="/test/path/file.json"):
            result = utils.get_transaction_list("/test/file.json")
            assert result == []


def test_get_transaction_list_type_error():
    """Тест обработки TypeError"""
    with patch("builtins.open", side_effect=TypeError):
        with patch("os.path.abspath", return_value="/test/path/file.json"):
            result = utils.get_transaction_list("/test/file.json")
            assert result == []


def test_get_transaction_list_value_error():
    """Тест обработки ValueError"""
    with patch("builtins.open", side_effect=ValueError):
        with patch("os.path.abspath", return_value="/test/path/file.json"):
            result = utils.get_transaction_list("/test/file.json")
            assert result == []

