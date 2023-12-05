#!/usr/bin/python3
"""json to string module"""


import json


def to_json_string(my_obj):
    """Return json object as string.


    Args:
        my_obj: object to convert.

    Return: oject
    """
    return json.dumps(my_obj)
