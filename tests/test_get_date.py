import pytest

from src.widget import get_date


def test_valid_data():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-11-03T02:26:18.671407") == "03.11.2024"


def test_no_t_data():
    with pytest.raises(ValueError):
        get_date("2024-03-11 02:26:18.671407")


def test_no_dash_data():
    with pytest.raises(ValueError):
        get_date("2024 03 11T02:26:18.671407")


def test_no_time_data():
    with pytest.raises(ValueError):
        get_date("2024-03-11")


def test_no_date_data():
    with pytest.raises(ValueError):
        get_date("02:26:18.671407")


def test_one_dash_data():
    with pytest.raises(ValueError):
        get_date("2024-11 03T02:26:18.671407")
