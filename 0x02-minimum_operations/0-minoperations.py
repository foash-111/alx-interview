#!/usr/bin/python3
"""min-operations"""


def minOperations(n):
    """min operation"""
    if n == 1 or n == 0:
        return 0
 
    count = 0
    if n != 2 and n % 2 != 0:
        counter = 3
        flag = 0
        while (counter < n):
            if n % counter == 0:
                flag = 1
                break
            counter += 2
        if flag != 1:
            return 0

    while (n % 3 == 0 and n != 0):
        count += 3
        n = n / 3
        if n == 1:
            n = 0

    while (n % 2 == 0 and n != 0):
        count += 2
        n = n / 2
        if n == 1:
            n = 0

    while (n > 0):
        n -= 1
        count += 1
    return count
