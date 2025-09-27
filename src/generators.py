# from data import transactions


def filter_by_currency(transactions, currency):
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    try:
        filtered_transactions = list(
            filter(lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions)
        )
        if not filtered_transactions:
            yield "No transactions with such currency"
        else:
            for transaction in filtered_transactions:
                yield transaction
    except KeyError:
        yield "Transactions list doesnt contain currency field. Impossible to filter by currency"


def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if not transactions:
        yield "Transaction list is empty"
    else:
        for item in transactions:
            try:
                yield item["description"]
            except KeyError:
                yield "<No description for this transaction>"


def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    try:
        if int(start) in range(1, 10000000000000000) and int(stop) in range(1, 10000000000000000):
            if int(start) <= int(stop):
                for num in range(int(start), int(stop) + 1):
                    num_str = f"{num:016d}"
                    formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
                    yield formatted_number
            else:
                yield "Start value must be less or equal to stop. Please try again"
        else:
            yield (
                "You have gone beyond the acceptable range of values."
                "Please enter start/stop values in range 1 - 9999 9999 9999 9999"
            )
    except ValueError:
        yield "You've entered  wrong start or stop value. Please enter digits only in range 1 - 9999 9999 9999 9999"


# user_currency = input("Please enter currency to filter: ")
# usd_transactions = filter_by_currency(transactions.test_transactions(), user_currency)
# for _ in range(len(transactions.test_transactions())):
#     print(next(usd_transactions, "Process finished"))


# descriptions = transaction_descriptions(transactions.test_transactions())
# for _ in range(len(transactions.test_transactions_no_description())):
#     print(next(descriptions, "Process finished"))

# range_start = input("Please enter range start, from 1 to 9999 9999 9999 9999: ")
# range_end = input("Please enter range end, from 1 to 9999 9999 9999 9999: ")
# for card_number in card_number_generator(range_start, range_end):
#     print(card_number)
