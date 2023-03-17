#!/usr/bin/python3
"""
This module defines square class
with a constructor method & arguments
"""


class Square:
    """
    This square validates data
    """

    def __init__(self, size=0):
        """
        The function __init__ is a constructor that initializes the size of the square
        :param size: The size of the square, defaults to 0 (optional)
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
