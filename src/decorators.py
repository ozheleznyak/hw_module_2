# import os
from functools import wraps
from time import ctime


def log(filename=None):
    def logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = ctime()
            try:
                result = func(*args, **kwargs)
                end_time = ctime()
                log_message = f'Start: {start_time}\n"{func.__name__}": OK\nEnd: {end_time}\n\n'
                if filename:
                    # file_path = os.path.join("..", "logs", filename)
                    with open("../logs/mylog.txt", "w", encoding='utf-8') as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as exception_message:
                end_time_exception = ctime()
                error_message = (f'Start: {start_time}\n"{func.__name__}": {exception_message}. '
                                 f'Inputs: {args}, {kwargs}\n{end_time_exception}\n\n')
                if filename:
                    # file_path_exception = os.path.join("..", "logs", filename)
                    with open("../logs/mylog.txt", "w", encoding='utf-8') as log_file:
                        log_file.write(error_message)
                else:
                    print(error_message)

        return wrapper

    return logging

