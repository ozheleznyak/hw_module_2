# from src import masks
# from src import widget
# from src import processing
from src import generators
from data import transactions

if __name__ == "__main__":
    # user_card_number = input("Enter your card number (16 digits without spaces): ")
    # print(masks.get_mask_card_number("1596837868705199"))
    # user_account_number = input("Enter your account number (only digits): ")
    # print(masks.get_mask_account(user_account_number))
    # transaction_date_format = input("Enter your transaction timestamp: ")
    # print(widget.get_date(transaction_date_format))
    # user_input = input("Enter your account or card number: ")
    # print(widget.mask_account_card(user_input))
    # print(mask_account_card('1111222233334444'))

    # user_input_transaction_list = [
    #     {"id": 41428829, "state": "EXECUTED"},
    #     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    #     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    #     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    # ]
    # user_input_state = input("Enter filter state or press Enter for default filter by EXECUTED: ")
    # if user_input_state:
    #     print(processing.filter_by_state(user_input_transaction_list, user_input_state))
    # else:
    #     print(processing.filter_by_state(user_input_transaction_list))
    # print()
    #
    # sorting_order = input("Press Y if you want ascending sorting: ")
    # if sorting_order == "Y":
    #     print(processing.sort_by_date(user_input_transaction_list, False))
    # else:
    #     print(processing.sort_by_date(user_input_transaction_list))

    user_currency = input("Please enter currency to filter: ")
    usd_transactions = generators.filter_by_currency(transactions.test_transactions(), user_currency)
    for _ in range(len(transactions.test_transactions())):
        print(next(usd_transactions))

    # descriptions = generators.transaction_descriptions(transactions.test_transactions())
    # for _ in range(len(transactions.test_transactions_no_description())):
    #     print(next(descriptions))
    #
    # range_start = input("Please enter range start, from 1 to 9999 9999 9999 9999: ")
    # range_end = input("Please enter range end, from 1 to 9999 9999 9999 9999: ")
    # for card_number in generators.card_number_generator(range_start, range_end):
    #     print(card_number)
