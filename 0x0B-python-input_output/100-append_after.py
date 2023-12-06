#!/usr/bin/python3
"""Append module"""


def append_after(filename="", search_string="", new_string=""):
    """Append method"""
    text = ""
    with open(filename, encoding="UTF8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode="w") as f:
        f.write(text)
