import pytest

import env
from pythonTest.matchers import assertNpEquals

from python.AdditionalCondition import AdditionalCondition
from python.Operator import Operator
from python.LinearProblem import LinearProblem
from python.TargetFunction import TargetFunction
from python.ProblemType import ProblemType
from python.PrimalSimplex import PrimalSimplex


def test_shouldDoSimplex_A1_2():
    tf = TargetFunction([2, 1, 3, 1, 2])
    ac1 = AdditionalCondition([1, 2, 1, 0, 1], Operator.SmallerThan, 100)
    ac2 = AdditionalCondition([0, 1, 1, 1, 1], Operator.SmallerThan, 80)
    ac3 = AdditionalCondition([1, 0, 1, 1, 0], Operator.SmallerThan, 50)
    lp = LinearProblem("A1_2", ProblemType.Maximize, tf, [ac1, ac2, ac3])
    simplex = PrimalSimplex(lp)
    (x, F) = simplex.solve()

    assertNpEquals(x, [20, 0, 30, 0, 50, 0, 0, 0])
    assert F == 230


def test_shouldDoSimplex_A1_3():
    tf = TargetFunction([10, 20])
    ac1 = AdditionalCondition([1, 1], Operator.SmallerThan, 100)
    ac2 = AdditionalCondition([6, 9], Operator.SmallerThan, 720)
    ac3 = AdditionalCondition([0, 1], Operator.SmallerThan, 60)
    lp = LinearProblem("A1_3", ProblemType.Maximize, tf, [ac1, ac2, ac3])
    simplex = PrimalSimplex(lp)
    (x, F) = simplex.solve()

    assertNpEquals(x, [30, 60, 10, 0, 0])
    assert F == 1500


def test_shouldDoSimplex_Example_MatheBibel_de():
    tf = TargetFunction([150, 100])
    ac1 = AdditionalCondition([16, 6], Operator.SmallerThan, 252)
    ac2 = AdditionalCondition([4, 12], Operator.SmallerThan, 168)
    lp = LinearProblem("MatheBibel", ProblemType.Maximize, tf, [ac1, ac2])
    simplex = PrimalSimplex(lp)
    (x, F) = simplex.solve()

    assertNpEquals(x, [12, 10, 0, 0])
    assert F == 2800


if __name__ == "__main__":
    pytest.main()
