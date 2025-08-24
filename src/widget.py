import masks

def mask_account_card():
    """"""


def get_date(transaction_date_format: str) -> str:
    """функция для преобразования таймстэмпа в формат DD.MM.YYYY без указания времени
    реализовано с учетом того, что у формата даты есть определнный шаблон"""
    only_date_by_user = ""
    i = 0

    while transaction_date_format[i] != "T":
        only_date_by_user += transaction_date_format[i]
        i += 1

    only_date_by_user_list = only_date_by_user.split("-")
    transformed_date_list = ".".join(only_date_by_user_list[-1::-1])

    return transformed_date_list
