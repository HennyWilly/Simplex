import pytest

import env
from python.ProblemType import ProblemType


def test_shouldGetToString_MinimizeProblem():
    assert str(ProblemType.Minimize) == "min."


def test_shouldGetToString_MaximizeProblem():
    assert str(ProblemType.Maximize) == "max."


if __name__ == "__main__":
    pytest.main()
