#!/usr/bin/python3
"""Module 9-rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle"""
    def __init__(self, width, height):
        """Initializes an instance."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate area of width and height"""
        return self.__width * self.__height

    def __str__(self):
        """print method"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
