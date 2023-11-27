#!/usr/bin/python3
"""Rectangle Class."""


class Rectangle:
    """Defines the blueprint of a rectangle.

    Attribute:
        width: An integer indicating the width of the rectangle object.
        height: An integer indicating the height of the rectangle object.
    """
    number_of_instance = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """An object constructor method.

        Initiatilizes Rectangle with width and height

        Args:
            width: An integer representing object width.
            height: An integer representing object height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instance += 1

    @property
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
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @propert
    def height(self):
        """Gets the height private attribute value.

        Return:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """A public object method.

        Returns:
            The current rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """A public object method.

        Returns:
            The current rectangle perimeter.
        """
        return 2 * (self.width + self.height) if self.width > 0 and
    self.height > 0 else 0

    def __str__(self):
        """Returns an informal and nicely printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.width):
            for j in range(self.height):
                rectangle.append(str(Rectangle.print_symbol))
            rectangle.append("\n")
        rectangle.pop()
        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: the rectangle representation
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Deletes an instance of a class"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Computes the area of two rectangles and compares them.

        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.

        Returns:
            Rectangle: the rectangle with the biggest area else rect_1 if
            areas are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise ValueError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance with width == height == size.

        Args:
            cls: used to access class attributes.
            size (int, optional): size of rectangle (1 side). Defaults to 0.

        Returns:
            Square: the new rectangle with equal values of height and width .
        """
        return cls(size, size)
