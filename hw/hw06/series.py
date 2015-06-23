#!/usr/bin/env python


def fibonacci(n):
    """Generate nth position of Fibonacci sequence"""
    sequence = [0, 1]
    sequence.extend([0] * (n - 2))
    if (n > 2):
        for i in range(2, n):
            sequence[i] = sequence[i - 2] + sequence[i - 1]
    return sequence[n-1]


def lucas(n):
    """Generate nth position of Lucas number series"""
    sequence = [2, 1]
    sequence.extend([0] * (n - 2))
    if (n > 2):
        for i in range(2, n):
            sequence[i] = sequence[i - 2] + sequence[i - 1]
    return sequence[n-1]

print(fibonacci(7))
print(lucas(6))
