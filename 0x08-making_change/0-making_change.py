#!/usr/bin/python3
"""iven a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total."""


# GPT enhancement
def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    counter = 0

    coins = sorted(coins, reverse=True)

    for coin in coins:
        if total > coin:
            counter += total // coin
            total = total % coin

        if total == 0:
            return counter

    return -1
