#!/usr/bin/python3
"""This module represents a square."""


class Rectangle:
    """Class that defines a square."""

    def __init__(self, width=0, height=0):
        """Iniatialize a new Rectangle object with the given width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Reactangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate and return are of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """calculate and return the perimeter of Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
