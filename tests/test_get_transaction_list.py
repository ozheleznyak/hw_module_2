from unittest.mock import patch
from src import utils




def test_get_transaction_list_success_with_mock_json_load():
    """"""
    file_path = "transactions.json"
    expected_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    with patch("os.path.abspath", return_value="/absolute/path/transactions.json"):
        with patch("builtins.open") as mock_open:
            with patch("json.load", return_value=expected_data):
                result = utils.get_transaction_list(file_path)

                assert result == expected_data
                mock_open.assert_called_once_with("/absolute/path/transactions.json", encoding="UTF-8")


