#!/usr/bin/python3
"""Save module"""


import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file.


    Args:
        my_obj: object to manipulate
        filename: text file.

    Return: object.
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        written = json.dump(my_obj, f)
    return written
