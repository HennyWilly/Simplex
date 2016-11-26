import pytest

import env
from python.PivotElement import PivotElement


def test_shouldNotCreatePivotElement_InvalidRow():
    with pytest.raises(ValueError):
        PivotElement(-1, 2, 100)


def test_shouldNotCreatePivotElement_InvalidColumn():
    with pytest.raises(ValueError):
        PivotElement(1, -2, 100)


def test_shouldCreatePivotElement():
    pivot = PivotElement(1, 2, 100)
    assert str(pivot) == "Pivot: row=1, col=2, value=100.00"


if __name__ == "__main__":
    pytest.main()
