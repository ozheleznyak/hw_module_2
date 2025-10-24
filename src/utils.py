import json
import os

from src import external_api


def get_transaction_list(file_path: str) -> list:
    """Функцию принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список"""
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


def transaction_amount(file_path: str) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях,
    тип данных — float. Для транзакций в валюте отличной от RUB, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли"""
    user_transaction = get_transaction_list(file_path)
    total_amount = 0.0

    for i in user_transaction:
        if i["operationAmount"]["currency"].get("code") == "RUB":
            total_amount += float(i["operationAmount"]["amount"])
        else:
            amount = i["operationAmount"]["amount"]
            currency_to_exchange = i["operationAmount"]["currency"]["code"]
            amount_exchange = external_api.external_api_exchange(amount=amount, from_currency=currency_to_exchange)
            total_amount += amount_exchange
    return total_amount
