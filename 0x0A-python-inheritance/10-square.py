#!/usr/bin/python3
"""Module 10-square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherits from Rectangle"""
    def __init__(self, size):
        """initialization method"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init(self.__size, self.__size)
