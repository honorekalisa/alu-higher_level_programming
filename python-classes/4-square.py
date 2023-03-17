#!/usr/bin/python3

"""
square module
"""


class Square:
    """
    class here
    """
    def __init__(self, size=0):
        """
        A constructor that initializes the size of the square.
        :param size: the size of the square matrix, defaults to 0 (optional)
        """
        
        self.__size = size

    @property
    def size(self):
        """
        This function returns the size of the list
        :return: The size of the square
        """
       
        return self.__size

    @size.setter
    def size(self, value):
        """
        The function size() takes in a value and checks if it is an integer. If it is not an integer, it
        raises a TypeError. If it is an integer, it checks if it is less than 0. If it is less than 0,
        it raises a ValueError. If it is not less than 0, it sets the value of size to the value of the
        argument.
        # Python
        def area(self):
                return self.__size ** 2
        :param value: The value to be assigned to the attribute
        """
        
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2
