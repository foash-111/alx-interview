#!/usr/bin/python3
"""
pascal triangle
# every index except the first and last index is the sum of
the index above and the (index - 1) of the above array
<array in the index before>
"""


def pascal_triangle(n):
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
