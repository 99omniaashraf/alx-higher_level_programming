#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board, N):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_util(board, 0, N)

def solve_util(board, row, N):
    if row == N:
        print_solution(board, N)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_util(board, row + 1, N)
            board[row][col] = 0

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    main()

