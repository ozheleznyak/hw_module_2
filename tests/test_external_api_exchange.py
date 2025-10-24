from unittest.mock import Mock, patch

import pytest
import requests

from src import external_api


def test_successful_conversion():
    """Тест успешного конвертирования валюты"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 75000.5}

    with patch('requests.get', return_value=mock_response):
        with patch.dict('os.environ', {'API_KEY': 'test_key'}):
            result = external_api.external_api_exchange('1000', 'USD')
            assert result == 75000.5


def test_rate_limit_exceeded():
    """Тест превышения лимита запросов"""
    mock_response = Mock()
    mock_response.status_code = 429

    with patch('requests.get', return_value=mock_response):
        with patch.dict('os.environ', {'API_KEY': 'test_key'}):
            with pytest.raises(Exception) as exc_info:
                external_api.external_api_exchange('1000', 'USD')
            assert 'Too many requests for your subscription' in str(exc_info.value)


def test_failed_request():
    """Тест неудачного запроса с другим кодом ошибки"""
    mock_response = Mock()
    mock_response.status_code = 500

    with patch('requests.get', return_value=mock_response):
        with patch.dict('os.environ', {'API_KEY': 'test_key'}):
            with pytest.raises(ValueError) as exc_info:
                external_api.external_api_exchange('1000', 'USD')
            assert 'Failed to get currency rate' in str(exc_info.value)


def test_network_error():
    """Тест ошибки сети"""
    with patch('requests.get', side_effect=requests.exceptions.RequestException()):
        with patch.dict('os.environ', {'API_KEY': 'test_key'}):
            with pytest.raises(requests.exceptions.RequestException):
                external_api.external_api_exchange('1000', 'USD')
