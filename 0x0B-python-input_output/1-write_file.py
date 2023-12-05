#!/usr/bin/python3
"""write method"""


def write_file(filename="", text=""):
    """write to file.


    Args:
        filename: file to read.
        text: string to write with.

    Return: number of character written.
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        if f.write(text):
            return len(text)
