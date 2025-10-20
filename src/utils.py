import json
import os

# from external_api import external_api_exchange

def get_transaction_list(file_path: str) -> list:
    """yyy"""
    transaction_list = []
    file_name = os.path.abspath(file_path)

    try:
        with open(file_name, encoding="UTF-8") as json_file:
            transaction_list = json.load(json_file)
        return transaction_list
    except json.JSONDecodeError:
        return transaction_list
    except TypeError:
        return transaction_list
    except ValueError:
        return transaction_list
    except FileNotFoundError:
        return transaction_list


# def transaction_amount(file_path: str) -> float:
#     """bbb"""
#     user_transaction = get_transaction_list(file_path)
#     transaction_amount = 0.0
#
#     for i in user_transaction:
#         if i["operationAmount"]["currency"].get("code") == "RUB":
#             transaction_amount += float(i["operationAmount"]["amount"])
#         else:
#             amount = i["operationAmount"]["amount"]
#             currency_to_exchange = i["operationAmount"]["currency"]["code"]
#             amount_exchange = external_api_exchange(amount=amount, from_currency=currency_to_exchange)
#             transaction_amount += amount_exchange
#     return transaction_amount


# y = transaction_amount("../data/operations.json")
y = get_transaction_list("../data/operations.json")
print(y)

