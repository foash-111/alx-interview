#!/usr/bin/python3
"""protect N queens from under attack each other"""

from sys import argv


def is_safe(board, row, col):
    """check if the col, right and left diagonal are safe"""

    # Check this column for any queens in previous rows
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the upper diagonal on the right side
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, N, positions, all_solutions):
    """check if it safe then append"""

    # Base case: if all queens are placed, return the solution
    if row == N:
        all_solutions.append(positions.copy())
        return

    # Consider each column in this row
    for col in range(N):
        if is_safe(board, row, col):
            # Place queen
            board[row][col] = 'Q'
            positions.append((row, col))

            # Recurse to place queens in the next row
            solve_nqueens(board, row + 1, N, positions, all_solutions)

            # Backtrack: remove the queen and try next column
            board[row][col] = '.'
            positions.pop()


def main():
    """maint method and start point"""

    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        N = int(argv[1])
        if N < 4:
            print('N must be at least 4')
            exit(1)
    except ValueError:
        print('N must be a number')
        exit(1)

    board = [['.' for i in range(N)] for j in range(N)]
    all_solutions = []
    solve_nqueens(board, 0, N, [], all_solutions)

    # Print all solutions
    for solution in all_solutions:
        print(solution)


main()
