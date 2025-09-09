import pytest

from src.processing import filter_by_state


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 615064591, "state": "EXECUTED", "date": "2017-10-14T08:21:33.419441"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2022-05-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-12-12T21:27:25.241689"},
            ],
        ),
        ("NEW", [{"id": 594226727, "state": "NEW", "date": "2025-07-10T21:27:25.241689"}]),
        ("PENDING", [{"id": 615064591, "state": "PENDING", "date": "2018-10-26T09:30:33.419441"}]),
        (
            "FAILED",
            [
                {"id": 594226727, "state": "FAILED", "date": "2018-08-17T21:27:25.241689"},
                {"id": 615064591, "state": "FAILED", "date": "2018-01-14T08:21:33.419441"},
            ],
        ),
        (
            "REFUNDED",
            [
                {"id": 594226727, "state": "REFUNDED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "REFUNDED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_valid_transactions_list_by_state(valid_transactions_list, state, expected):
    assert filter_by_state(valid_transactions_list, state) == expected


def test_no_state(valid_transactions_list):
    assert filter_by_state(valid_transactions_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "EXECUTED", "date": "2017-10-14T08:21:33.419441"},
    ]


def test_no_such_state(valid_transactions_list):
    assert filter_by_state(valid_transactions_list, 'ERROR') == []


def test_existing_state_lower_case(valid_transactions_list):
    assert filter_by_state(valid_transactions_list, 'pending') == [{"id": 615064591, "state": "PENDING", "date": "2018-10-26T09:30:33.419441"}]


def test_invalid_characters_state(valid_transactions_list):
    assert filter_by_state(valid_transactions_list, '!@#$%^&*') == []
