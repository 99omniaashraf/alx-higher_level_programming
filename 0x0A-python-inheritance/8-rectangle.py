#!/usr/bin/python3
"""Module 7-base_geometry"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """ raises an Exception with the message
        'area() is not implemented'.
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Module 8-rectangle"""


class Rectangle(BaseGeometry):
    """Represent a rectangle.
    private instance attributes:
        width
        height
    Inherites from BaseGeometry.
    """
    def __init__(self, width, height):
        """Initializes an instance.


        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
