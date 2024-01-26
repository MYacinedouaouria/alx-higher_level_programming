#!/usr/bin/python3
""" this module provide a class definition Square"""


class Square:
    """ a simple square class"""

    def __init__(self, size=0):
        """ initialisation of a square"""

        if isinstance(size, int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ returns the current square area"""

        return self.__size ** 2
