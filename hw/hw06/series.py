#!/usr/bin/env python


def fibonacci(n):
    sequence = list(range(0, n))
    print(sequence)
    if (n > 2):
        for i in range(2, n):
            sequence[i] = sequence[i - 2] + sequence[i - 1]
            print(i, sequence)
    return sequence[n-1]

print(fibonacci(7))
