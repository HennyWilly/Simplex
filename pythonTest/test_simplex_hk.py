import pytest

import env
from python.simplex_hk import simplex
from matchers import assertNpEquals

def test_shouldNotDoSimplex_fNotHasEnoughEntries():
    A = [1, 2, 3]
    b = [1]
    f = [1]
    with pytest.raises(ValueError):
        simplex(A, b, f)


def test_shouldNotDoSimplex_bHasNotEnoughEntries():
    A = [[1], [2], [3]]
    b = [1]
    f = [1]
    with pytest.raises(ValueError):
        simplex(A, b, f)


def test_shouldNotDoSimplex_bContainsNegativeValues():
    A = [1, 2, 3]
    b = [-1]
    f = [1, -1, 2]
    with pytest.raises(ValueError):
        simplex(A, b, f)


def test_shouldDoSimplex_A1_2():
    A = [[1, 2, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 0, 0, 0, 1]]
    b = [100, 80, 50]
    f = [-2, -1, -3, -1, -2, 0, 0, 0]

    (ARes, bRes, fRes, res) = simplex(A, b, f)
    assertNpEquals(ARes, [[1, 1, 0, -1, 0, 1, -1, 0], [0, 2, 0, -1, 1, 1, 0, -1], [0, -1, 1, 2, 0, -1, 1, 1]])
    assertNpEquals(bRes, [20, 50, 30])
    assertNpEquals(fRes, [0, 2, 0, 1, 0, 1, 1, 1])
    assert res == 230


def test_shouldDoSimplex_A1_3():
    A = [[1, 1, 1, 0, 0], [6, 9, 0, 1, 0], [0, 1, 0, 0, 1]]
    b = [100, 720, 60]
    f = [-10, -20, 0, 0, 0]

    (ARes, bRes, fRes, res) = simplex(A, b, f)
    assertNpEquals(ARes, [[0, 0, 1, -1.0 / 6, 1.0 / 2], [1, 0, 0, 1.0 / 6, -3.0 / 2], [0, 1, 0, 0, 1]])
    assertNpEquals(bRes, [10, 30, 60])
    assertNpEquals(fRes, [0, 0, 0, 5.0 / 3, 5])
    assert res == 1500


def test_shouldDoSimplex_Example_MatheBibel_de():
    A = [[16, 6, 1, 0], [4, 12, 0, 1]]
    b = [252, 168]
    f = [-150, -100, 0, 0]

    (ARes, bRes, fRes, res) = simplex(A, b, f)
    assertNpEquals(ARes, [[1, 0, 1.0 / 14, -1.0 / 28], [0, 1, -1.0 / 42, 2.0 / 21]])
    assertNpEquals(bRes, [12, 10])
    assertNpEquals(fRes, [0, 0, 25.0 / 3, 25.0 / 6])
    assert res == 2800


if __name__ == "__main__":
    pytest.main()
