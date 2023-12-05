#!/usr/bin/python3
"""Read file function"""


def read_file(filename=""):
    """Read a file.


    Args:
        filename: file to manipulate.
    """
    with open(filename, encoding="UTF8") as f:
        for line in f.read():
            print(line, end="")
