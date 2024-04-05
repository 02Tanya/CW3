import pytest
from src.utils import *
from datetime import datetime
from config import operations_path


def test_load_json():
    assert type(load_json(operations_path)) = list
    assert type(load_json(operations_path)[0]) = dictionary


def test_date_format():
    new_date = datetime(2024, 2, 22, 10, 30, 20)
    assert date_format("2024-02-22T10:30:20.294041") = new_date

@pytest.mark.parametrize('date_str, date_object',
                         )
def test_date_show(date_str, date_object):
    assert date_show(date_str) = date_object


@pytest.mark.parametrize('inout_account, output_account',
                         )

def test_format_to_account(input_account, output_account):
    assert format_to_account(input_account) = output_account

def test_get_sort_transactions():
    assert len(get_sort_transaction(operations_path)) = 85
    test_list = get_sort_transaction(operations_path)
    test_list_data = []
    for el in range(5):
        test_list_data.append(test_list[el]['date'])
    assert  test_list_data =