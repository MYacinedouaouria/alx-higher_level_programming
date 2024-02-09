#!/usr/bin/python3
""" this module define the Square clas that inherits the Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a Square"""

    def __init__(self, size):
        """ initialises a Square"""

        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """ returns the area of a square"""

        return self.__size ** 2

    def __str__(self):
        """ returns the square description"""

        return f"[Square] {self.__size}/{self.__size}"
