#!/usr/bin/python3

"""
square module
"""


class Square:
    """
    square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        This function creates a square with a size and position.

        :param size: the size of the square, defaults to 0 (optional)
        :param position: a tuple of 2 positive integers;
        """

        self.__size = size
        self.__add_position(position)

    @property
    def position(self):
        return self.__position

    def __add_position(self, position):
        """
        It adds a position to the portfolio.

        :param position: a tuple of (x, y) coordinates
        """

        error_text = "position must be a tuple of 2 positive integers"
        # Check if it is a tuple
        if isinstance(position, tuple):

            # Check if it is of length 2
            if len(position) == 2:
                # Check if both values are ints
                first_is_int = isinstance(position[0], int)
                second_is_int = isinstance(position[1], int)

                if first_is_int and second_is_int:

                    # Check if values are both > 0
                    if position[0] >= 0 and position[1] >= 0:

                        self.__position = position
                    else:
                        raise TypeError(error_text)
                else:
                    raise TypeError(error_text)
            else:
                raise TypeError(error_text)
        else:
            raise TypeError(error_text)

    @position.setter
    def position(self, position):
        self.__add_position(position)

    @property
    def size(self):
        """
        Square2 now can inherit properties
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        *|MARKER_CURSOR|*

        :param value: The value of the parameter
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
            for i in range(self.position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
