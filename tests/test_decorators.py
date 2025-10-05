import re
import pytest

from src.decorators import log


def test_log_decorator_console(capsys):
    """проверяем, что в консоль выводится правильный лог, если с аргументами все ОК"""
    @log()
    def my_function(x, y):
        return x + y

    my_function(3, 4)
    captured = capsys.readouterr()
    assert re.search(r'"my_function"', captured.out)
    assert re.search(r"OK", captured.out)


def test_log_decorator_exception_console(capsys):
    """проверяем, что в консоль выводится правильный лог, если функция завершается с ошибкой. Ожидаем, что обнаружится слово Inputs"""
    @log()
    def my_function(x, y):
        return x + y

    my_function("3", "4")
    captured = capsys.readouterr()
    assert re.search(r'"Inputs"', captured.out)
