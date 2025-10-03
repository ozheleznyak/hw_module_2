# from data import transactions


def filter_by_currency(transactions, currency):
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"].get("name") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for item in transactions:
        yield item.get("description", "<No description for this transaction>")


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
                print("Start value must be less or equal to stop. Please try again")
        else:
            print(
                "You have gone beyond the acceptable range of values."
                "Please enter start/stop values in range 1 - 9999 9999 9999 9999"
            )
    except ValueError:
        print("You've entered  wrong start or stop value. Please enter digits only in range 1 - 9999 9999 9999 9999")


# user_currency = input("Please enter currency to filter: ")
# usd_transactions = filter_by_currency([], "ghj")
# for _ in range(len(transactions.test_transactions_no_currency())):
#     print(next(usd_transactions, "Process finished")
# print(next(usd_transactions, "Process finished"))


# descriptions = transaction_descriptions([])
# for _ in range(len([])):
# print(next(descriptions, "Process finished"))

# range_start = input("Please enter range start, from 1 to 9999 9999 9999 9999: ")
# range_end = input("Please enter range end, from 1 to 9999 9999 9999 9999: ")
# for card_number in card_number_generator(5, 1):
#     print(card_number)
