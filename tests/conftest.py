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
