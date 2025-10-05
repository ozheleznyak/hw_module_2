import pytest

from src.generators import card_number_generator


def test_normal_usage_card_number_generator():
    """тестируем типичное использование генератора для допустимых значений диапазона"""
    generator = card_number_generator(2, 5)
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


def test_min_min_card_number_generator():
    """тестируем использование генератора при начальном и конечном значениях равных 0"""
    generator = card_number_generator(1, 1)
    assert next(generator) == "0000 0000 0000 0001"


def test_max_max_card_number_generator():
    """тестируем использование генератора при начальном и конечном значениях равных 9999 9999 9999 9999"""
    generator = card_number_generator(9999999999999999, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9999"


def test_wrong_symbols_card_number_generator():
    """проверка, когда хотя бы одно из значений символьное"""
    generator = card_number_generator("bvc", 5)
    with pytest.raises(StopIteration):
        next(generator)


def test_out_of_range_card_number_generator():
    """проверка, когда хотя бы одно значение выходит за предел допустимого диапазона"""
    generator = card_number_generator(-1, 5)
    with pytest.raises(StopIteration):
        next(generator)


def test_stop_less_start_card_number_generator():
    """проверка, когда конечное значение меньше начального"""
    generator = card_number_generator(10, 2)
    with pytest.raises(StopIteration):
        next(generator)
