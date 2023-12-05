#!/usr/bin/python3
"""Json module"""


import json


def from_json_string(my_str):
    """Convert str to object.


    Args:
        my_str: string to convert.

    Return: object.
    """
    return json.loads(my_str)
