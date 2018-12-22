"""Unit test cases for fibo."""

from fibo import fibo


def test_fibo_small_number():
    """Test cases with small-size numbers."""
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8
    assert fibo(7) == 13


def test_fibo_big_number():
    """Test cases with big-size numbers."""
    assert fibo(30) == 832040
