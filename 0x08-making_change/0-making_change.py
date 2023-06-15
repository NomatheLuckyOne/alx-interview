#!/usr/bin/python3
"""Making change"""

def makeChange(coins, total):
    """A function that returns the minimum operations"""
    if total < 0:
        return 0

    num_of_ops = 0
    coins.sort(reverse=True)
    for value in coins:
        if total % value <= total:
            num_of_ops += total // value
            total = total % value

    if total == 0:
        return num_of_ops
    return -1
