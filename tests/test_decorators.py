import os
import re

import pytest

from src.decorators import log


def test_log_decorator_console(capsys):
    """проверяем, что в консоль выводится правильный лог, если с аргументами все ОК.
    Ожидаем, что обнаружится название функции my_function и слово OK"""
    @log()
    def my_function(x, y):
        return x + y

    my_function(3, 4)
    captured = capsys.readouterr()
    assert re.search(r'"my_function"', captured.out)
    assert re.search(r'OK', captured.out)


def test_log_decorator_exception_console(capsys):
    """проверяем, что в консоль выводится правильный лог, если функция завершается с ошибкой.
    Ожидаем, что обнаружится конструкция "Inputs: ('3', '4')",
    потому что я перестаралась и решила вывести в лог еще и время начала
    и окончания выполнения функции, а это динамический параметр и вряд ли совпадет )))"""
    @log()
    def my_function(x, y):
        return x / y

    my_function("3", "4")
    captured = capsys.readouterr()
    assert re.search(r"Inputs: \('3', '4'\)", captured.out)


def test_log_decorator_txt():
    """проверяем, что в текстовый файл выводится правильный лог, если с параметрами все ОК.
    Ожидаем, что обнаружится название функции my_function и слово OK"""
    # file_path = os.path.join("..", "logs", "mylog.txt")
    @log("mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(3, 4)
    with open("../logs/mylog.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert '"my_function"' in content
    assert 'OK' in content


def test_log_decorator_exception_txt():
    """проверяем, что в текстовый файл выводится правильный лог, если с параметрами все ОК.
    Ожидаем, что обнаружится название функции my_function и конструкция Inputs: ('3', '4'),
    подтверждающая, что это формат лога об ошибке"""
    # file_path = os.path.join("..", "logs", "mylog.txt")
    @log("mylog.txt")
    def my_function(x, y):
        return x / y

    my_function('3', '4')
    with open("../logs/mylog.txt", "r", encoding="utf-8") as f:
        content = f.read()
    assert '"my_function"' in content
    assert "Inputs: ('3', '4')" in content