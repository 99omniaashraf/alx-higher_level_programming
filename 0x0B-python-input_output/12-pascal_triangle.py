#!/usr/bin/python3
"""Plascal's triangle module"""


def pascal_triangle(n):
    """Calculate pascal.


    Args:
        n: value

    Return: list
    """
    my_lisst = []
    if n <= 0:
        return my_lisst
    for i in range(n):
        num = 11 ** i
        li = [int(n) for n in str(num)]
        my_lisst.append(li)
    return my_lisst
