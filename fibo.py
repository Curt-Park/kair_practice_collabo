"""Abstract fibo function."""


def fibo(n: int) -> int:
    """Return the result of fibonaci series."""
    n1, n2 = 0, 1

    for _ in range(n):
        n2, n1 = n1 + n2, n2

    return n1
