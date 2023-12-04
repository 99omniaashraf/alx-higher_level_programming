#!/usr/bin/python3
"""Module 0-lookup"""


def lookup(obj):
    """Returns the list of available attributes and methods.


    Args:
        obj: object to look into.
    """
    return dir(obj)
