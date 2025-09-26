from data import transactions


def filter_by_currency(transactions: list, currency: str):
    "Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."
    filtered_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions))
    for transaction in filtered_transactions:
        yield transaction


def transaction_descriptions(transactions: list):
    for item in transactions:
        yield item["description"]


def card_number_generator(start, stop):
    "Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."
    "Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."

    for num in range(int(start), int(stop) + 1):
        num_str = f"{num:016d}"
        formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted_number

    # user_currency = input("Please enter currency to filter: ")


# usd_transactions = filter_by_currency(transactions.test_transactions(), user_currency) # обойти излишний вызов функции. мерять длинну списка транзцакций, запускать цикл по длинне и обрабатывать ошибку
# избыточных прогонов

# descriptions = transaction_descriptions(transactions.test_transactions())

# for _ in range(len(transactions.test_transactions())):
#     # print(next(usd_transactions))
#     print(next(descriptions))

range_start = input("Please enter range start: ")
range_end = input("Please enter range end: ")
for card_number in card_number_generator(range_start, range_end):
    print(card_number)