import pytest

import env
from python.TargetFunction import TargetFunction
from python.Operator import Operator
from matchers import assertNpEquals


def test_shouldNotCreateTargetFunction_StringPassed():
    condition = TargetFunction("F(x1..x5) = 10x1 - 20x2 + 30x3 - 40x4 + 50x5")
    # TODO Should we raise an error here?


def test_shouldCreateTargetFunction():
    condition = TargetFunction([10, -20, 30, -40, 50])
    assert condition.getNumberOfCoeffs() == 5
    assert str(condition) == "F(x1..x5) = 10x1 -20x2 + 30x3 -40x4 + 50x5 "


if __name__ == "__main__":
    pytest.main()