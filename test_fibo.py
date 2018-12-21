"""Sample test to run pytest on Travis-CI."""

from fibo import fibo


def test_fibo_small_numbers():
    """Test fibo(n), where n in [1, 10]."""
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8
    assert fibo(7) == 13
    assert fibo(8) == 21
    assert fibo(9) == 34
    assert fibo(10) == 55


def test_fibo_big_numbers():
    """Test fibo(n), where n in {20, 25, 30, 40}."""
    assert fibo(20) == 6765
    assert fibo(25) == 75025
    assert fibo(30) == 832040
    assert fibo(40) == 102334155
