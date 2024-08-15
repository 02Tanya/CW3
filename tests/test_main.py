from config import operations_path
from src.main import *

def test_five_transactions():
    assert len(five_transactions(operations_path)) = 5

def test_get_transactions():
    assert get_transaction(operations_path) = ()