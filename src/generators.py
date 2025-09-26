from data import transactions


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
            yield ("You have gone beyond the acceptable range of values."
                   "Please enter start/stop values in range 1 - 9999 9999 9999 9999")
    except ValueError:
        yield "You've entered  wrong start or stop value. Please enter digits only in range 1 - 9999 9999 9999 9999"

    # user_currency = input("Please enter currency to filter: ")


usd_transactions = filter_by_currency(
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ],
    "USD",
)  # обойти излишний вызов функции. мерять длинну списка транзцакций, запускать цикл по длинне и обрабатывать ошибку
# избыточных прогонов
# for _ in range(len(transactions.test_transactions())):
#     print(next(usd_transactions))


descriptions = transaction_descriptions(transactions.test_transactions_no_description())

for _ in range(len(transactions.test_transactions_no_description())):
    # print(next(usd_transactions))
    print(next(descriptions))

# range_start = input("Please enter range start: ")
# range_end = input("Please enter range end: ")
# for card_number in card_number_generator(0, 1111222233334445):
#     print(card_number)
