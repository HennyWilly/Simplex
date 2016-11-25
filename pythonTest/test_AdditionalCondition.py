import pytest

import env
from python.AdditionalCondition import AdditionalCondition
from python.Operator import Operator


def test_shouldNotCreateAdditionalCondition_StringPassed():
    with pytest.raises(TypeError):
        AdditionalCondition("F(x1..x5) = 10x1 -20x2 + 30x3 -40x4 + 50x5")


def test_shouldCreateAdditionalCondition_SmallerThan():
    condition = AdditionalCondition([1, -2, 3, -4], Operator.SmallerThan, 100)
    assert condition.getNumberOfCoeffs() == 4
    assert str(condition) == "1x1 -2x2 + 3x3 -4x4 <= 100"


def test_shouldCreateAdditionalCondition_Smaller():
    condition = AdditionalCondition([1, -2, 3, -4], Operator.Smaller, 100)
    assert condition.getNumberOfCoeffs() == 4
    assert str(condition) == "1x1 -2x2 + 3x3 -4x4 < 100"


def test_shouldCreateAdditionalCondition_GreaterThan():
    condition = AdditionalCondition([1, -2, 3, -4], Operator.GreaterThan, 100)
    assert condition.getNumberOfCoeffs() == 4
    assert str(condition) == "1x1 -2x2 + 3x3 -4x4 >= 100"


def test_shouldCreateAdditionalCondition_Greater():
    condition = AdditionalCondition([1, -2, 3, -4], Operator.Greater, 100)
    assert condition.getNumberOfCoeffs() == 4
    assert str(condition) == "1x1 -2x2 + 3x3 -4x4 > 100"


def test_shouldCreateAdditionalCondition_Equals():
    condition = AdditionalCondition([1, -2, 3, -4], Operator.Equals, 100)
    assert condition.getNumberOfCoeffs() == 4
    assert str(condition) == "1x1 -2x2 + 3x3 -4x4 = 100"


def test_shouldCreateAdditionalCondition_UnknownOperator():
    condition = AdditionalCondition([1, -2, 3, -4], Operator.Unknown, 100)
    assert condition.getNumberOfCoeffs() == 4
    assert str(condition) == "1x1 -2x2 + 3x3 -4x4 <Operator.Unknown> 100"


if __name__ == "__main__":
    pytest.main()