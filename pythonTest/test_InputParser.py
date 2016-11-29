import pytest

import env
from pythonTest.matchers import assertNpEquals

from python.InputParser import parseLines, parseAdditionalConditionStr, parseTargetFunctionStr, parseCoeffs, \
    parseNumberOfCoeffs, parseOperator, parseRhs
from python.ProblemType import ProblemType
from python.Operator import Operator

commentedOutExample = """# Exercise 1.01 a)
                         #max. F(x1..x2) = 4x1 + 3x2
                         #x1 + 3x2 <= 9
                         #-x1 + 2x2 >= 2"""

maximizeExample = """# Exercise 1.01 b)
                     max. F(x1..x2)= 2x1 + x2
                     -x1 + x2 <= 1
                     x1 + 3x2 >= 6"""

minimizeExample = """# Exercise 2.01 b)
                     min. F(x1..x3)= x1 + x2 + 3x3
                     x1 - x2 >= 10
                     x1 - x3 >= 12"""


def test_shouldParseLines_CommentedOut():
    parsed = parseLines(commentedOutExample.split('\n'))
    assert len(parsed) == 0


def test_shouldParseString_MaximizeProblem():
    parsed = parseLines(maximizeExample.split('\n'))
    assert len(parsed) == 1

    maxProblem = parsed[0]
    assert maxProblem.description == "# Exercise 1.01 b)"
    assert maxProblem.problemType == ProblemType.Maximize
    assertNpEquals(maxProblem.targetFunction.coeffs, [2, 1])
    assert len(maxProblem.additionalConditions) == 2

    ac1 = maxProblem.additionalConditions[0]
    assertNpEquals(ac1.coeffs, [-1, 1])
    assert ac1.operator is Operator.SmallerThan
    assert ac1.rhs == 1

    ac2 = maxProblem.additionalConditions[1]
    assertNpEquals(ac2.coeffs, [1, 3])
    assert ac2.operator is Operator.GreaterThan
    assert ac2.rhs == 6


def test_shouldParseString_MinimizeProblem():
    parsed = parseLines(minimizeExample.split('\n'))
    assert len(parsed) == 1

    minProblem = parsed[0]
    assert minProblem.description == "# Exercise 2.01 b)"
    assert minProblem.problemType == ProblemType.Minimize
    assertNpEquals(minProblem.targetFunction.coeffs, [1, 1, 3])
    assert len(minProblem.additionalConditions) == 2

    ac1 = minProblem.additionalConditions[0]
    assertNpEquals(ac1.coeffs, [1, -1, 0])
    assert ac1.operator is Operator.GreaterThan
    assert ac1.rhs == 10

    ac2 = minProblem.additionalConditions[1]
    assertNpEquals(ac2.coeffs, [1, 0, -1])
    assert ac2.operator is Operator.GreaterThan
    assert ac2.rhs == 12


def test_shouldParseString_MultipleProblems():
    bigString = "{}\n\n{}\n\n{}".format(commentedOutExample, maximizeExample, minimizeExample)
    parsed = parseLines(bigString.split('\n'))

    # I assume the LinearProblem objects are ok, because we already checked them separately
    assert len(parsed) == 2


def test_shouldParseAdditionalCondition():
    tf = parseAdditionalConditionStr("x1-20x2+30x3-5x5<=10", 5)
    assertNpEquals(tf.coeffs, [1, -20, 30, 0, -5])
    assert tf.operator is Operator.SmallerThan
    assert tf.rhs == 10


def test_shouldParseAdditionalCondition_FillMissingCoeffsWithZeros():
    tf = parseAdditionalConditionStr("x1-20x2+30x3-5x5>=15", 10)
    assertNpEquals(tf.coeffs, [1, -20, 30, 0, -5, 0, 0, 0, 0, 0])
    assert tf.operator is Operator.GreaterThan
    assert tf.rhs == 15


def test_shouldParseAdditionalCondition_IgnoreBiggerThenNumberOfCoeffs():
    tf = parseAdditionalConditionStr("x1-20x2+30x3-5x5=25", 3)
    assertNpEquals(tf.coeffs, [1, -20, 30])
    assert tf.operator is Operator.Equals
    assert tf.rhs == 25


def test_shouldParseTargetFunction():
    tf = parseTargetFunctionStr("F(x1..x5)=x1-20x2+30x3-5x5")
    assertNpEquals(tf.coeffs, [1, -20, 30, 0, -5])


def test_shouldParseTargetFunction_MoreArgsInLhs():
    tf = parseTargetFunctionStr("F(x1..x6)=x1-20x2+30x3-5x5")
    assertNpEquals(tf.coeffs, [1, -20, 30, 0, -5, 0])


def test_shouldParseTargetFunction_LessArgsInLhs():
    tf = parseTargetFunctionStr("F(x1..x4)=x1-20x2+30x3-5x5")
    assertNpEquals(tf.coeffs, [1, -20, 30, 0])


def test_shouldParseCoeffs():
    assertNpEquals(parseCoeffs("x1-20x2+30x3-5x5", 5), [1, -20, 30, 0, -5])


def test_shouldParseCoeffs_IgnoreBiggerThenNumberOfCoeffs():
    assertNpEquals(parseCoeffs("x1-20x2+30x3-5x5", 3), [1, -20, 30])


def test_shouldParseNumberOfCoeffs():
    assert parseNumberOfCoeffs("F(x1..x5)") == 5


def test_shouldParseNumberOfCoeffs_OneArg():
    assert parseNumberOfCoeffs("F(x1..x1)") == 1


def test_shouldParseNumberOfCoeffs_NotStartingAtOne():
    assert parseNumberOfCoeffs("F(x2..x5)") == 4


def test_shouldNotParseNumberOfCoeffs_WrongOrdner():
    with pytest.raises(ValueError):
        parseNumberOfCoeffs("F(x5..x1)")


def test_shouldParseOperator_SmalerThan():
    assert parseOperator("<=") is Operator.SmallerThan


def test_shouldParseOperator_Smaler():
    assert parseOperator("<") is Operator.Smaller


def test_shouldParseOperator_GreaterThan():
    assert parseOperator(">=") is Operator.GreaterThan


def test_shouldParseOperator_Greater():
    assert parseOperator(">") is Operator.Greater


def test_shouldParseOperator_Equals():
    assert parseOperator("=") is Operator.Equals


def test_shouldNotParseOperator_Unknown():
    assert parseOperator("abcd1234") is Operator.Unknown


def test_shouldParseRhs_SmalerThan():
    assert parseRhs("x <= 10", Operator.SmallerThan) == 10


def test_shouldParseRhs_Smaler():
    assert parseRhs("x < 10", Operator.Smaller) == 10


def test_shouldParseRhs_GreaterThan():
    assert parseRhs("x >= 10", Operator.GreaterThan) == 10


def test_shouldParseRhs_Greater():
    assert parseRhs("x > 10", Operator.Greater) == 10


def test_shouldParseRhs_Equals():
    assert parseRhs("x = 10", Operator.Equals) == 10


def test_shouldNotParseRhs_Unknown():
    assert parseRhs("x ? 10", Operator.Unknown) == 0


if __name__ == "__main__":
    pytest.main()
