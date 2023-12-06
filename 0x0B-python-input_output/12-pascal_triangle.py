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

    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(triangle[x - 1][y - 1] + triangle[x - 1][y])
        row.append(1)
        triangle.append(row)
    return triangle
