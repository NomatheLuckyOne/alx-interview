#!/usr/bin/python3
"""
a function to print Pascal's Triangle
"""


def pascal_triangle(n):
    """a p[ython function that prints
    Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
