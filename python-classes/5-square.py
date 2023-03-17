#!/usr/bin/python3

"""
square module
"""


# It creates a class called Square.
class Square:
    """
    square class
    """

    def __init__(self, size=0):
        """
        Size property is optional because size
        does not matter
        """
        self.__size = size

    @property
    def size(self):
        """
        This function returns the size of the stack
        :return: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        :param value: The value to be assigned to the attribute
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
