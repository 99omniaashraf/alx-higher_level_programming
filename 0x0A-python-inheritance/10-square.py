#!/usr/bin/python3
"""Module 10-square"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherits from Rectangle"""
    def __init__(self, size):
        """initialization method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init(self.__size, self.__size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return supper().__str__()
