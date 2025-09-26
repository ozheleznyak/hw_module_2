from data import transactions


def filter_by_currency(transactions: list, currency: str):
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    filtered_transactions = list(filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions))
    for transaction in filtered_transactions:
        yield transaction


def transaction_descriptions(transactions: list):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for item in transactions:
        yield item["description"]


def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    if int(start) in range(0, 1000000000000000) and int(stop) in range(0, 1000000000000000):
        if int(start) <= int(stop):
            try:
                for num in range(int(start), int(stop) + 1):
                    num_str = f"{num:016d}"
                    formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
                    yield formatted_number
            except ValueError:
                yield "You've entered  wrong start or stop value. Please enter digits only in range 0 - 9999 9999 9999 9999"
        else:
            yield "Start value must be less than stop. Please try again"
    else:
        yield "You have gone beyond the acceptable range of values. Please enter start/stop values in range 0 - 9999 9999 9999 9999"

    # user_currency = input("Please enter currency to filter: ")


# usd_transactions = filter_by_currency(transactions.test_transactions(), user_currency) # обойти излишний вызов функции. мерять длинну списка транзцакций, запускать цикл по длинне и обрабатывать ошибку
# избыточных прогонов

# descriptions = transaction_descriptions(transactions.test_transactions())

# for _ in range(len(transactions.test_transactions())):
#     # print(next(usd_transactions))
#     print(next(descriptions))

# range_start = input("Please enter range start: ")
# range_end = input("Please enter range end: ")
for card_number in card_number_generator(5, 1):
    print(card_number)