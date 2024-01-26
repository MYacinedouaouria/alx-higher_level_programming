#!/usr/bin/python3
"""contain the definition of the clas Square and its methods"""


class Square:
    """define a Square class"""

    def __init__(self, size=0):
        """ inisialisation of a Square"""

        self.size = size

    @property
    def size(self):
        """ retrive the size of the square"""

        return self.__size

    @size.setter
    def size(self, size=0):
        """sets the attribute size of the square"""
        if isinstance(size, int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the area of the current square"""

        return self.size ** 2
