#!/usr/bin/python3
"""Rectangle Class.

This module contains an empty class that defines a rectangle.
"""


class Rectangle:
    """Defines the blueprint of a rectangle.

    Attribute:
        width: An integer indicating the width of the rectangle object.
        height: An integer indicating the height of the rectangle object.
    """
    def __init__(self, width=0, height=0):
        """An object constructor method.

        Initiatilizes Rectangle with width and height

        Args:
            width: An integer representing object width.
            height: An integer representing object height.
        """
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character.
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        rec_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += "#"
            rec_str += "\n"
        return rec_str[:-1]

    @propert
    def width(self):
        """Gets the width private attribute value.

        Returns:
            The width private attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width private attribute value.

        Validates the assignment of the width private attribute.

        Args:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @propert
    def height(self):
        """Gets the height private attribute value.

        Returns:
            The height private attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height private attribute value.

        Validates the assignment of the height private attribute.

        Args:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A public object method.

        Returns:
            The current rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """A public object method.

        Returns:
            The current rectangle perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
