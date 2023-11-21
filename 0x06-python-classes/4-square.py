#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.


        Args:
            size (int): The size of the new square.

        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.size)

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return (self.__size * self.__size)
