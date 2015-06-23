#!/usr/bin/env python


def fibonacci(n):
    """
    Description:
        Sum a Fibonacci series of numbers

    Args:
        n: The element of the series to return

    Returns:
        Sum of the previous two elements in the series
    """
    sequence = [0, 1]
    if (n > 1):
        sequence.extend([0] * (n - 1))
        for i in range(2, n+1):
            sequence[i] = sequence[i - 2] + sequence[i - 1]
    return sequence[n]


def lucas(n):
    """
    Description:
        Sum a Lucas series of numbers

    Args:
        n: The element of the series to return

    Returns:
        Sum of the previous two elements in the series
    """
    sequence = [2, 1]
    if (n > 1):
        sequence.extend([0] * (n - 1))
        for i in range(2, n+1):
            sequence[i] = sequence[i - 2] + sequence[i - 1]
    return sequence[n]


def sum_series(n, i=0, j=1):
    """
    Description:
        Sum a series of numbers

    Args:
        n: The element of the series to return
        i: The first element of the series (Optional)
        j: The second element of the series (Optional)

    Returns:
        Sum of the previous two elements in the series
    """
    sequence = [i, j]
    if (n > 1):
        sequence.extend([0] * (n - 1))
        for i in range(2, n+1):
            sequence[i] = sequence[i - 2] + sequence[i - 1]
    return sequence[n]
