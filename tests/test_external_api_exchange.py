from unittest.mock import patch
from src import external_api


@patch('requests.get')
def test_external_api_exchange(mock_get):
    """"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': 100.00}
    assert external_api.external_api_exchange('USD', '10') == 100.00
    # mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10&apikey=mbU2HKyaQBQPJaBT7fSDJFW4u0igJhBD')