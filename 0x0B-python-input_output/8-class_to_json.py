#!/usr/bin/python3
"""Json module"""


def class_to_json(obj):
    """Returns dict description data structure.


    Args:
        obj: an instance of a Class.

    Return: object serialized.
    """
    return vars(obj)
