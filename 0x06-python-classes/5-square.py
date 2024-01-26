#!/usr/bin/python3
""" this module provides class Square definition"""


class Square:
    """ a simple square class"""

    def __init__(self, size=0):
        """ initialize the Square"""

        self.size = size

    @property
    def size(self):
        """ retrive the size of the square"""

        return self.__size

    @size.setter
    def size(self, size=0):
        """sets the size of the square"""

        if isinstance(size, int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ returns the current square area"""
        return self.__size * 2

    def my_print(self):
        """ prints in stdout the square with tha char #"""
        if (self.size == 0):
            print()
        for i in range(self.size):
            for j in range(self.size - 1):
                print("#", end="")
            print("#")
