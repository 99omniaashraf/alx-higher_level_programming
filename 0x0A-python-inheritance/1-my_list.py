#!/usr/bin/python3
"""Module 1-my_list"""


class MyList(list):
    """Class MyList inherits from list."""

    def print_sorted(self):
        """prints the list, but sorted"""

        new_list = self[:]
        new_list.sorted()
        print("{}".format(new_list))
