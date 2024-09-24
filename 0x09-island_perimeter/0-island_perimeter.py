#!/usr/bin/python3
"""find island perimeter"""


def island_perimeter(grid):
    """find island perimeter"""
    perimeter = 0
    flag = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j]) == 1 and flag == 0:
                perimeter += 4
                flag = 1
                # set flag to 1 to not enter this condition again
            try:
                if grid[i][j] == 1:
                    if (grid[i][j - 1] == 1) != (grid[i - 1][j] == 1):
                        perimeter += 2
            except IndexError:
                pass

    return perimeter
