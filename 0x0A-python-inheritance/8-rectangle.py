#!/usr/bin/python3
"""Module 8-rectangle"""


BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


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
        self.width = width
        self.height = height
