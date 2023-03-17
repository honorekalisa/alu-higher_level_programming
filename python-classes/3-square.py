#!/usr/bin/python3

"""
This module defines the square class
"""


class Square:
    """
    This patented square class
    """
    def __init__(self, size=0):
        """
        If the size is not an integer, raise a TypeError exception with the message
        size must be an integer. 
        :param size: The size of the square, defaults to 0 (optional)
        """
       
        # Check if size is not an int
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        # Check if size is negative
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        The function area() returns the area of the square
        :return: The area of the square.
        """
       
        return self.__size ** 2
