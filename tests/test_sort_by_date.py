from src.processing import sort_by_date


def test_sort_descending(valid_transactions_list):
    assert sort_by_date(valid_transactions_list, True) == [
        {"date": "2025-07-10T21:27:25.241689", "id": 594226727, "state": "NEW"},
        {"date": "2022-05-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-12-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-26T09:30:33.419441", "id": 615064591, "state": "PENDING"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "REFUNDED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "REFUNDED"},
        {"date": "2018-08-17T21:27:25.241689", "id": 594226727, "state": "FAILED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-01-14T08:21:33.419441", "id": 615064591, "state": "FAILED"},
        {"date": "2017-10-14T08:21:33.419441", "id": 615064591, "state": "EXECUTED"},
    ]


def test_sort_ascending(valid_transactions_list):
    assert sort_by_date(valid_transactions_list, False) == [
        {"date": "2017-10-14T08:21:33.419441", "id": 615064591, "state": "EXECUTED"},
        {"date": "2018-01-14T08:21:33.419441", "id": 615064591, "state": "FAILED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-08-17T21:27:25.241689", "id": 594226727, "state": "FAILED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "REFUNDED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "REFUNDED"},
        {"date": "2018-10-26T09:30:33.419441", "id": 615064591, "state": "PENDING"},
        {"date": "2018-12-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2022-05-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2025-07-10T21:27:25.241689", "id": 594226727, "state": "NEW"},
    ]


def test_sort_no_state_provided(valid_transactions_list):
    assert sort_by_date(valid_transactions_list) == [
        {"date": "2025-07-10T21:27:25.241689", "id": 594226727, "state": "NEW"},
        {"date": "2022-05-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-12-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-26T09:30:33.419441", "id": 615064591, "state": "PENDING"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "REFUNDED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "REFUNDED"},
        {"date": "2018-08-17T21:27:25.241689", "id": 594226727, "state": "FAILED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-01-14T08:21:33.419441", "id": 615064591, "state": "FAILED"},
        {"date": "2017-10-14T08:21:33.419441", "id": 615064591, "state": "EXECUTED"},
    ]


def test_no_date_list(no_date_value_transactions_list):
    assert sort_by_date(no_date_value_transactions_list) == [
        {"date": "", "id": 41428829, "state": "EXECUTED"},
        {"date": "", "id": 939719570, "state": "EXECUTED"},
        {"date": "", "id": 594226727, "state": "CANCELED"},
    ]


def test_one_date_missing(one_date_value_missing):
    assert sort_by_date(one_date_value_missing, False) == [
        {"date": "", "id": 939719570, "state": "EXECUTED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2022-05-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
    ]


def test_no_date_key_transaction_list(no_date_key):
    assert sort_by_date(no_date_key) == [
        {"id": 41428829, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED"},
    ]


def test_no_time_transaction_list(no_time_transactions_list):
    assert sort_by_date(no_time_transactions_list) == [
        {"date": "2022-05-12", "id": 594226727, "state": "CANCELED"},
        {"date": "2019-07-03", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-06-30", "id": 939719570, "state": "EXECUTED"},
    ]


def test_only_time_transactions_list(only_time_transactions_list):
    assert sort_by_date(only_time_transactions_list) == [
        {"date": "21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]


def test_date_with_dots_transactions_list(date_with_dots_transactions_list):
    assert sort_by_date(date_with_dots_transactions_list) == [
        {"date": "2022.05.12", "id": 594226727, "state": "CANCELED"},
        {"date": "2019.07.03", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018.06.30", "id": 939719570, "state": "EXECUTED"},
    ]
