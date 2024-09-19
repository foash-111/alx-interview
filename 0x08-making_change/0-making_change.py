#!/usr/bin/python3
"""iven a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total."""


def makeChange(coins, total):
	"""Return: fewest number of coins needed to meet total"""
	if total <= 0:
		return 0
	counter = 0
	while(total > 0 and len(coins) > 0):
		max_item = max(coins)
		if total >= max_item:
			counter += total // max_item
			total = total % max_item
			coins.remove(max_item)
		elif len(coins) > 1:
			coins.remove(max_item)

	if total > 0:
		return -1
	return counter
