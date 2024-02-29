#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers using binary search.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - A peak value from the list, if found. Otherwise, returns None.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
