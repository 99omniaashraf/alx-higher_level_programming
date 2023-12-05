#!/usr/bin/python3
"""Append module"""


def append_write(filename="", text=""):
    """Append to file with text.


    Args:
        filename: add to this object.
        text: string to append.

    Return: number of characters added
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        if f.write(text):
            return len(text)
