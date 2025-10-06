import os
from functools import wraps
from time import ctime


def log(filename=None):
    """декоратор записывает в файл или выводит в консоль имя функции и результат выполнения при успешной операции.
    Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке."""
    def logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = ctime()
            try:
                result = func(*args, **kwargs)
                end_time = ctime()
                log_message = f'Start: {start_time}\n"{func.__name__}": OK\nResult: {result}\nEnd: {end_time}\n\n'
                if filename:
                    file_path = os.path.join(os.path.dirname(__file__), "../logs", filename)
                    with open(file_path, "w", encoding="utf-8") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as exception_message:
                end_time_exception = ctime()
                error_message = (
                    f'Start: {start_time}\n"{func.__name__}": {exception_message}. '
                    f"Inputs: {args}, {kwargs}\n{end_time_exception}\n\n"
                )
                if filename:
                    file_path_exception = os.path.join(os.path.dirname(__file__), "../logs", filename)
                    with open(file_path_exception, "w", encoding="utf-8") as log_file:
                        log_file.write(error_message)
                else:
                    print(error_message)

        return wrapper

    return logging


# @log("log.txt")
# def my_function(x, y):
#     return x / y
#
#
# my_function(1, 2)
