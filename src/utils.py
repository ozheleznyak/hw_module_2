import json
import logging
import os

from src import external_api

# создаем логгер, обработчик и форматтер
logger = logging.getLogger('main')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/main.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')

# подключаем обработчик и форматер к логеру
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_list(file_path: str) -> list:
    """Функцию принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список"""

    transaction_list = []
    file_name = os.path.abspath(file_path)

    try:
        logger.info(f'Считываем данные из указанного файла: {file_path}')
        with open(file_name, encoding="UTF-8") as json_file:
            transaction_list = json.load(json_file)
        logger.info(f'Список считанных транзакций:\n{transaction_list}')
        return transaction_list
    except json.JSONDecodeError:
        logger.error(f'Ошибка преобразования данных из {file_path}')
        return transaction_list
    except TypeError:
        logger.error(f'Ошибка. Неподдерживаемый тип данных в {file_path}')
        return transaction_list
    except ValueError:
        logger.error(f'Ошибка. Некорректные данные в {file_path}')
        return transaction_list
    except FileNotFoundError:
        logger.error(f'Ошибка. Отсутствует {file_path}')
        return transaction_list


def transaction_amount(file_path: str) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях,
    тип данных — float. Для транзакций в валюте отличной от RUB, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли"""

    logger.info(f'Считываем данные из указанного файла: {file_path}')
    user_transaction = get_transaction_list(file_path)
    logger.info(f'Список считанных транзакций:\n{user_transaction}')

    total_amount = 0.0

    logger.info('Начало подсчета суммы транзакций')
    for i in user_transaction:
        if i["operationAmount"]["currency"].get("code") == "RUB":
            total_amount += float(i["operationAmount"]["amount"])
        else:
            amount = i["operationAmount"]["amount"]
            currency_to_exchange = i["operationAmount"]["currency"]["code"]
            amount_exchange = external_api.external_api_exchange(amount=amount, currency=currency_to_exchange)
            total_amount += amount_exchange
    return total_amount