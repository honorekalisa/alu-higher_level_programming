#!/usr/bin/python3
"""This module represents a rectangle."""


class Rectangle:
    """Defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize an instance of Rectangle with width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or setwidth of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Getter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get or set height of the height attribete."""
        return self.__height

    @height.setter
    def height(self, value):
        """Getter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns string representation of the rectangle using # character.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            rectangle = ''
            for i in range(self.height):
                rectangle += '#' * self.width + '\n'
            return rectangle[:-1]
