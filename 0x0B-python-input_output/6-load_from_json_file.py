#!/usr/bin/python3
"""Create object module"""


import json


def load_from_json_file(filename):
    """Create object method.


    Args:
        filename: file to deserialize.

    Return: object.
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        return json.load(f)
