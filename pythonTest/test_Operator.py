import pytest

import env
from python.Operator import Operator


def test_shouldGetToString_GreaterThan():
    assert str(Operator.GreaterThan) == ">="


def test_shouldGetToString_Greater():
    assert str(Operator.Greater) == ">"


def test_shouldGetToString_SmallerThan():
    assert str(Operator.SmallerThan) == "<="


def test_shouldGetToString_Smaller():
    assert str(Operator.Smaller) == "<"


def test_shouldGetToString_Equals():
    assert str(Operator.Equals) == "="


def test_shouldGetToString_UnknownOperator():
    assert str(Operator.Unknown) == "<Operator.Unknown>"


if __name__ == "__main__":
    pytest.main()
