import pytest

import env
from python.AdditionalCondition import AdditionalCondition
from python.Operator import Operator
from matchers import assertNpEquals


def test_shouldNotParseEquationStr_InvalidString():
    condition = AdditionalCondition("abcdef", 5)
    # TODO Should we raise an error here?


def test_shouldNotParseEquationStr_MultipleOperators():
    condition = AdditionalCondition("1x1 - 2x2 + 3x3 - 4x4 <= 100 <= 200", 4)
    # TODO Should we raise an error here?


def test_shouldParseCoeffs():
    condition = AdditionalCondition("1x1 - 2x2 + 3x3 - 4x4 <= 100", 4)
    assertNpEquals(condition.coeffs, [1, -2, 3, -4])


def test_shouldParseCoeffs_MoreCoeffsInStringThanPassed():
    condition = AdditionalCondition("5x1 - 2x2 + x5 <= 100", 3)
    assertNpEquals(condition.coeffs, [5, -2, 0])


def test_shouldParseCoeffs_LessCoeffsInStringThanPassed():
    condition = AdditionalCondition("5x1 - 2x2 <= 100", 5)
    assertNpEquals(condition.coeffs, [5, -2, 0, 0, 0])


def test_shouldParseOperator_SmallerThan():
    condition = AdditionalCondition("x1 <= 100", 1)
    assert condition.operator is Operator.SmallerThan


def test_shouldParseOperator_Smaller():
    condition = AdditionalCondition("x1 < 100", 1)
    assert condition.operator is Operator.Smaller


def test_shouldParseOperator_GreaterThan():
    condition = AdditionalCondition("x1 >= 100", 1)
    assert condition.operator is Operator.GreaterThan


def test_shouldParseOperator_Greater():
    condition = AdditionalCondition("x1 > 100", 1)
    assert condition.operator is Operator.Greater


def test_shouldParseOperator_Equals():
    condition = AdditionalCondition("x1 = 100", 1)
    assert condition.operator is Operator.Equals


def test_shouldParseOperator_UnknownOperator():
    condition = AdditionalCondition("x1 ? 100", 1)
    assert condition.operator is Operator.Unknown


def test_shouldParseRhs():
    condition = AdditionalCondition("x1 <= 100", 1)
    assert condition.result == 100


def test_shouldNotParseRhs_UnknownOperator():
    condition = AdditionalCondition("x1 ? 100", 1)
    assert condition.result == 0


if __name__ == "__main__":
    pytest.main()