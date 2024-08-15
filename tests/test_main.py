import pytest
import src.utils
import src.main


def test_main():
    assert print(src.main.main()) == None
