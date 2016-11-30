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

def test_isValidSolution():
    # Arrange
    conditionSmaller = AdditionalCondition([1, 1, 1, 1], Operator.Smaller, 41)
    conditionSmallerThan = AdditionalCondition([1, 1, 1, 1], Operator.SmallerThan, 40)
    conditionGreater = AdditionalCondition([1, 1, 1, 1], Operator.Greater, 39)
    conditionGreaterThan = AdditionalCondition([1, 1, 1, 1], Operator.GreaterThan, 40)
    conditionEquals = AdditionalCondition([1, 1, 1, 1], Operator.Equals, 40)
    # Act
    isValidSmaller = conditionSmaller.isValidSolution([10, 10, 10, 10])
    isValidSmallerThan = conditionSmallerThan.isValidSolution([10, 10, 10, 10])
    conditionGreater = conditionGreater.isValidSolution([10, 10, 10, 10])
    conditionGreaterThan = conditionGreaterThan.isValidSolution([10, 10, 10, 10])
    isValidEqauls = conditionEquals.isValidSolution([10, 10, 10, 10])
    # Assert
    assert isValidSmaller
    assert isValidSmallerThan
    assert conditionGreater
    assert conditionGreaterThan
    assert isValidEqauls

if __name__ == "__main__":
    pytest.main()
