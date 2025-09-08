from src import masks


def mask_account_card(user_input: str) -> str:
    """функция определяет какой тип данных был подан на вход (карта или счет)
    и в зависимости от типа возвращает в замаскированном виде
    реализация основана на определении количества казанных цифр,
    т.к. они фиксированы и отличаются для счета и для карты"""
    user_input_digits_only = ""
    user_input_text = ""

    for i in user_input:
        if i.isdigit():
            user_input_digits_only += i
        else:
            user_input_text += i

    if len(user_input_text) == 0:
        raise IndexError("You didn't entered card or account name")
    if len(user_input_digits_only) == 16 and user_input_text[-1] == " ":
        return user_input_text + masks.get_mask_card_number(user_input_digits_only)
    elif len(user_input_digits_only) == 20 and user_input_text[-1] == " ":
        return user_input_text + masks.get_mask_account(user_input_digits_only)
    else:
        raise ValueError("You've entered wrong data. Please try again")


def get_date(transaction_date_format: str) -> str:
    """функция для преобразования таймстэмпа в формат DD.MM.YYYY без указания времени
    реализовано с учетом того, что у формата даты есть определённый шаблон"""
    only_date_by_user = ""
    transformed_date_list = ""
    i = 0

    if transaction_date_format.count("T"):
        while transaction_date_format[i] != "T":
            only_date_by_user += transaction_date_format[i]
            i += 1
    else:
        raise ValueError("Wrong date format")

    if only_date_by_user.count("-") == 2:
        only_date_by_user_list = only_date_by_user.split("-")
    else:
        raise ValueError("Wrong date format, dash is missing")

    transformed_date_list = ".".join(only_date_by_user_list[-1::-1])

    return transformed_date_list
