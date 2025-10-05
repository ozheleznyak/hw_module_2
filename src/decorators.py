from functools import wraps
from time import time

def log(filename):
    def logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            try:
                result = func(*args, **kwargs)
                end_time = time()
                log_message = f'{start_time}\n"{func.__name__}": {result}. Inputs: {args}, {kwargs}\n{end_time}'
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)
                return result
            except Exception as exception_message:
                end_time_exception = time()
                error_message = f'{start_time}\n"{func.__name__}": {exception_message}. Inputs: {args}, {kwargs}\n{end_time_exception}'
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(error_message)
                else:
                    print(error_message)
        return wrapper
    return logging


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)