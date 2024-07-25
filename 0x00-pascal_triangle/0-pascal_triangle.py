#!/usr/bin/python3
"""
pascal triangle

# every index except the first and last index is the sum of
the index above and the (index - 1) of the above array
<array in the index before>

Usage:
    To use this script, call the `pascal_triangle(n)` function
    with the desired number of rows.

 Example:
        >>> pascal_triangle(5)
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
"""


def pascal_triangle(n):
    """ Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists,
        where each inner list represents a row in Pascal's Triangle.
    """
    if n <= 0:
        return []
    else:
        great_list = []
        for i in range(n):
            inner_list = [1] * (i + 1)
            for j in range(i):
                if j == 0 or j == i:
                    inner_list[j] = 1
                else:
                    inner_list[j] =\
                        great_list[i - 1][j - 1] + great_list[i - 1][j]
            great_list.append(inner_list)
        return great_list
