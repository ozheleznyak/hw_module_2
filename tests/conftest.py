import pytest


@pytest.fixture
def card_number():
    return "1111222233334444"


@pytest.fixture
def account_number():
    return "12345678901234567890"


@pytest.fixture
def invalid_card_number():
    return ["", "qqqqwwwweeeerrrr", "1234567890", "1111 2222 3333 4444", "!@#$%^&*()_+_)(*"]


@pytest.fixture
def invalid_account_number():
    return ["", "qqqqwwwweeeerrrr", "1234567890", "1111 2222 3333 4444", "!@#$%^&*()_+_)(*"]


@pytest.fixture
def valid_transactions_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2022-05-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "NEW", "date": "2025-07-10T21:27:25.241689"},
        {"id": 615064591, "state": "PENDING", "date": "2018-10-26T09:30:33.419441"},
        {"id": 594226727, "state": "FAILED", "date": "2018-08-17T21:27:25.241689"},
        {"id": 615064591, "state": "FAILED", "date": "2018-01-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-12-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2017-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "REFUNDED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "REFUNDED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def no_date_value_transactions_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": ""},
        {"id": 939719570, "state": "EXECUTED", "date": ""},
        {"id": 594226727, "state": "CANCELED", "date": ""},
    ]


@pytest.fixture
def one_date_value_missing():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": ""},
        {"id": 594226727, "state": "CANCELED", "date": "2022-05-12T21:27:25.241689"},
    ]


@pytest.fixture
def no_date_key():
    return [
        {"id": 41428829, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED"},
    ]


@pytest.fixture
def no_time_transactions_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
        {"id": 594226727, "state": "CANCELED", "date": "2022-05-12"},
    ]


@pytest.fixture
def only_time_transactions_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "21:27:25.241689"},
    ]


@pytest.fixture
def date_with_dots_transactions_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019.07.03"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018.06.30"},
        {"id": 594226727, "state": "CANCELED", "date": "2022.05.12"},
    ]


@pytest.fixture
def test_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def test_transactions_no_currency():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07"},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93"},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def test_transactions_no_description():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07"},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93"},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93"},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.fixture
def test_transactions_no_descriptions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07"},
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93"},
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
