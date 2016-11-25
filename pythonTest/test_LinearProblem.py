import pytest
from matchers import assertNpEquals

import env
from python.ProblemType import ProblemType
from python.TargetFunction import TargetFunction
from python.Operator import Operator
from python.AdditionalCondition import AdditionalCondition
from python.LinearProblem import LinearProblem


def test_shouldCreatePivotElement():
    pt = ProblemType.Maximize
    tf = TargetFunction([1, -2, 3, -4])
    acs = [AdditionalCondition([1, -2, -3, 0], Operator.SmallerThan, 10), AdditionalCondition([0, -1, -2, 4], Operator.SmallerThan, 15)]
    lp = LinearProblem("Test", pt, tf, acs)

    expectedString = "Test\n" + "max. F(x1..x4) = 1x1 -2x2 + 3x3 -4x4 \n" + "1x1 -2x2 -3x3 + 0x4 <= 10\n" + "0x1 -1x2 -2x3 + 4x4 <= 15\n"
    assert str(lp) == expectedString

def test_shouldNormalizeTargetFunction_MinimalizeProblem():
    pt = ProblemType.Minimize
    tf = TargetFunction([1, -2, 3, -4])
    lp = LinearProblem("Test", pt, tf, [])

    normalized = lp.normalize()
    assert normalized.problemType == ProblemType.Maximize
    assertNpEquals(normalized.targetFunction.coeffs, [-1, 2, -3, 4])

def test_shouldNormalizeTargetFunction_MaximizeProblem():
    pt = ProblemType.Maximize
    tf = TargetFunction([1, -2, 3, -4])
    lp = LinearProblem("Test", pt, tf, [])

    normalized = lp.normalize()
    assert normalized.problemType == ProblemType.Maximize
    assertNpEquals(normalized.targetFunction.coeffs, [1, -2, 3, -4])

if __name__ == "__main__":
    pytest.main()