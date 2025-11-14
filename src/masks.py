import logging

# создаем логгер, обработчик и форматтер
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')

# подключаем обработчик и форматер к логеру
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(user_card_number: str) -> str:
    """функция для создания маски номера карты по типу XXXX XX** **** XXXX
    реализованна из расчета, что номер карты всегда содержит 16 цифр"""

    logger.info(f'Создаем маску для корректно введенного номера карты "{user_card_number}"')
    if user_card_number.isdigit() and len(user_card_number) == 16:
        user_card_number_list = [i for i in user_card_number]
        user_card_number_list[6:12] = [
            "*",
            "*",
            "*",
            "*",
            "*",
            "*",
        ]
        for n in range(len(user_card_number_list)):
            if n == 4 or n == 9 or n == 14:
                user_card_number_list.insert(n, " ")
        masked_user_card_number = "".join(user_card_number_list)
        logger.info(f'Создана маска карты: {masked_user_card_number}')
        return masked_user_card_number
    else:
        logger.error(f'Ошибка. Введен неверный формат карты: {user_card_number}')
        raise ValueError("You've entered wrong card number. Please try again")


def get_mask_account(user_account_number: str) -> str:
    """функция для создания маски номера счета по типу **XXXX
    реализованна из расчета, что номер счета всегда содержит 20 цифр"""

    logger.info(f'Создаем маску для корректно введенного номера счета "{user_account_number}"')
    if user_account_number.isdigit() and len(user_account_number) == 20:
        user_account_number_list = [i for i in user_account_number[-6:]]

        for n in range(len(user_account_number_list) - 4):
            user_account_number_list[n] = "*"
        masked_user_account_number = "".join(user_account_number_list)
        logger.info(f'Создана маска счета: {masked_user_account_number}')
        return masked_user_account_number
    else:
        logger.error(f'Ошибка. Введен неверный формат счета: {user_account_number}')
        raise ValueError("You've entered wrong account number. Please try again")
