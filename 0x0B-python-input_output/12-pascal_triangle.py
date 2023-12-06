#!/usr/bin/python3
"""Plascal's triangle module"""


def pascal_triangle(n):
    """Calculate pascal.


    Args:
        n: value

    Return: list
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row - [1]
        for i in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
