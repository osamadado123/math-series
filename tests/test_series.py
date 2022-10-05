import pytest
from math_series.series import fibonacci,lucas,sum_series


def test_one ():
    actual = fibonacci(3)
    expected = "2"
    assert str(actual)==expected
def test_two ():
    actual = fibonacci(4)
    expected = "3"
    assert str(actual)==expected
def test_three ():
    actual = fibonacci(5)
    expected = "5"
    assert str(actual)==expected
def test_four ():
    actual = fibonacci(6)
    expected = "8"
    assert str(actual)==expected
def test_five ():
    actual = fibonacci(7)
    expected = "13"
    assert str(actual)==expected
def test_six ():
    actual = fibonacci(8)
    expected = "21"
    assert str(actual)==expected
def test_seventeen ():
    actual = fibonacci(17)
    expected = "1597"
    assert str(actual)==expected
def test_lucas_one():
    actual = lucas(1)
    expected = "1"
    assert str(actual)==expected
def test_lucas_seven():
     actual = lucas(7)
     expected = "29"
     assert str(actual)==expected
def test_lucas_fourteen():
    actual = lucas(14)
    expected = "843"
    assert str(actual)==expected
def test_lucas_zero():
    actual = lucas(0)
    expected = "2"
    assert str(actual)==expected
def test_sum_one():
    actual = sum_series(7,2,1)
    expected = "29"
    assert str(actual)==expected
def test_sum_two():
    actual = sum_series(17)
    expected = "1597"
    assert str(actual)==expected
def test_sum_three():
    actual = sum_series(4,5,6)
    expected = "28"
    assert str(actual)==expected

def test_sum_eight ():
    actual = sum_series(8,5,6)
    expected = "191"
    assert str(actual)==expected