#!/usr/bin/python3
"""min-operations"""


def minOperations(n):
    """min operation"""
    count = 0
    if n != 2 and n % 2 != 0:
        count = 3
        while (count <= n):
            if count % n == 0:
                break
            count += 2
        return 0

    while (n % 3 == 0 and n != 0):
        count += 3
        n = n / 3

    while (n != 0 and n % 2 == 0):
        count += 2
        n = n / 2

    return count
