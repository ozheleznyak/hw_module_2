from src import masks
from src import widget

if __name__ == "__main__":
    # user_card_number = input("Enter your card number (16 digits without spaces): ")
    # print(masks.get_mask_card_number(user_card_number))
    # user_account_number = input("Enter your account number (only digits): ")
    # print(masks.get_mask_account(user_account_number))
    transaction_date_format = input("Enter your transaction timestamp: ")
    print(widget.get_date(transaction_date_format))