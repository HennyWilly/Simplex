import pytest

import env
from pythonTest.matchers import assertNpEquals

from python.ProblemType import ProblemType
from python.TargetFunction import TargetFunction
from python.Operator import Operator
from python.AdditionalCondition import AdditionalCondition
from python.LinearProblem import LinearProblem


def test_shouldCreateLinearProblem():
    pt = ProblemType.Maximize
    tf = TargetFunction([1, -2, 3, -4])
    acs = [AdditionalCondition([1, -2, -3, 0], Operator.SmallerThan, 10),
           AdditionalCondition([0, -1, -2, 4], Operator.SmallerThan, 15)]
    lp = LinearProblem("Test", pt, tf, acs)

    expectedString = "Test\n" + "max. F(x1..x4) = 1x1 -2x2 + 3x3 -4x4 \n" + "1x1 -2x2 -3x3 + 0x4 <= 10\n" + "0x1 -1x2 -2x3 + 4x4 <= 15\n"
    assert str(lp) == expectedString


def test_shouldNormalizeTargetFunction_MinimalizeProblem():
    pt = ProblemType.Minimize
    tf = TargetFunction([1, -2, 3, -4])
    lp = LinearProblem("Test", pt, tf, [])

    lp.normalize()
    assert lp.problemType == ProblemType.Maximize
    assertNpEquals(lp.targetFunction.coeffs, [-1, 2, -3, 4])


def test_shouldNormalizeTargetFunction_MaximizeProblem():
    pt = ProblemType.Maximize
    tf = TargetFunction([1, -2, 3, -4])
    lp = LinearProblem("Test", pt, tf, [])

    lp.normalize()
    assert lp.problemType == ProblemType.Maximize
    assertNpEquals(lp.targetFunction.coeffs, [1, -2, 3, -4])


def test_shouldNormalizeAdditionalCondition_SmallerThan():
    pt = ProblemType.Maximize
    tf = TargetFunction([1, -2, 3, -4])
    acs = [AdditionalCondition([-1, 2, -3], Operator.SmallerThan, 10.5)]
    lp = LinearProblem("Test", pt, tf, acs)

    lp.normalize()
    assert len(lp.additionalConditions) == 1

    nAc = lp.additionalConditions[0]
    assertNpEquals(nAc.coeffs, [-1, 2, -3])
    assert nAc.operator == Operator.SmallerThan
    assert nAc.rhs == 10.5


def test_shouldNormalizeAdditionalCondition_GreaterThan():
    pt = ProblemType.Maximize
    tf = TargetFunction([1, -2, 3, -4])
    acs = [AdditionalCondition([-1, 2, -3], Operator.GreaterThan, 10.5)]
    lp = LinearProblem("Test", pt, tf, acs)

    lp.normalize()
    assert len(lp.additionalConditions) == 1

    nAc = lp.additionalConditions[0]
    assertNpEquals(nAc.coeffs, [1, -2, 3])
    assert nAc.operator == Operator.SmallerThan
    assert nAc.rhs == -10.5


def test_shouldNormalizeAdditionalCondition_Equals():
    pt = ProblemType.Maximize
    tf = TargetFunction([1, -2, 3, -4])
    acs = [AdditionalCondition([-1, 2, -3], Operator.Equals, 10.5)]
    lp = LinearProblem("Test", pt, tf, acs)

    lp.normalize()
    assert len(lp.additionalConditions) == 2

    nAc1 = lp.additionalConditions[0]
    assertNpEquals(nAc1.coeffs, [-1, 2, -3])
    assert nAc1.operator == Operator.SmallerThan
    assert nAc1.rhs == 10.5

    nAc2 = lp.additionalConditions[1]
    assertNpEquals(nAc2.coeffs, [1, -2, 3])
    assert nAc2.operator == Operator.SmallerThan
    assert nAc2.rhs == -10.5


if __name__ == "__main__":
    pytest.main()
