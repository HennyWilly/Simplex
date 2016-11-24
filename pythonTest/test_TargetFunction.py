import pytest

import env
from python.TargetFunction import TargetFunction
from python.Operator import Operator
from matchers import assertNpEquals


def test_shouldNotParseEquationStr_InvalidString():
    condition = TargetFunction("abcdef")
    # TODO Should we raise an error here?


def test_shouldNotParseEquationStr_MultipleOperators():
    condition = TargetFunction("F(x1..x4) = 1x1 - 2x2 + 3x3 - 4x4 = 100 = 200")
    # TODO Should we raise an error here?


def test_shouldParseCoeffs():
    condition = TargetFunction("F(x1..x5) = 10x1 - 20x2 + 30x3 - 40x4 + 50x5")
    assert condition.numberOfCoeffs == 5
    assertNpEquals(condition.coeffs, [10, -20, 30, -40, 50])


def test_shouldParseCoeffs_MoreCoeffsRhsThanLhs():
    condition = TargetFunction("F(x1..x9) = 10x1 - 20x2")
    assert condition.numberOfCoeffs == 9
    assertNpEquals(condition.coeffs, [10, -20, 0, 0, 0, 0, 0, 0, 0])


def test_shouldNotParseCoeffs_MoreCoeffsLhsThanRhs():
    condition = TargetFunction("F(x1..x2) = 10x1 - 20x2 + 30x3")
    # TODO Should we raise an error here?


if __name__ == "__main__":
    pytest.main()