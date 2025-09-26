from src.generators import card_number_generator

def test_normal_usage_card_number_generator():
    """тестируем типичное использование генератора для допустимых значений диапазона"""
    generator = card_number_generator(2, 5)
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    assert next(generator) == "0000 0000 0000 0004"
    assert next(generator) == "0000 0000 0000 0005"


def test_min_min_usage_card_number_generator():
    """тестируем использование генератора при начальном и конечном значениях равных 0"""
    generator = card_number_generator(0, 0)
    assert next(generator) == "0000 0000 0000 0000"


def test_max_max_usage_card_number_generator():
    """тестируем использование генератора при начальном и конечном значениях равных 9999 9999 9999 9999"""
    generator = card_number_generator(9999999999999999, 9999999999999999)
    assert next(generator) == "9999 9999 9999 9999"