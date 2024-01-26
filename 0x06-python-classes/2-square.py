#!/usr/bin/python3
""" this module contain definition of the class Square"""


class Square:
    """ a simple class square"""

    def __init__(self, size=0):
        """initialize the Square"""

        if isinstance(size, int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
