import pytest
import src.utils


def test_load_operations():
    assert type(src.utils.load_operations()) == list
    assert type(src.utils.load_operations()[0]) == dict


@pytest.fixture
def data_transaction():
    return "2019-08-26T10:50:58.294041"


def test_show_date(data_transaction):
    assert src.utils.show_date(data_transaction) == "26-08-2019"


@pytest.fixture
def card_number():
    return "Maestro 1596837868705199"


def test_get_card_number(card_number):
    assert src.utils.get_card_number(card_number) == "Maestro 1596 83** **** 5199"
#    assert src.utils.get_card_number(None) = null


@pytest.fixture
def account_number():
    return "Счет 64686473678894779589"


def test_get_account_number(account_number):
    assert src.utils.get_account_number(account_number) == "Счет **9589"


def test_sorted_transactions():
    assert len(src.utils.get_sorted_transactions()) == 85
