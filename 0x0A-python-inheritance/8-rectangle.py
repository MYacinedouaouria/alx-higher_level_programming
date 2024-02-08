#!/usr/bin/python3
""" tis module define a class Rectangle that inherit
    BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle , inherits BaseGeometry"""

    def __init__(self, width, height):
        """ initialize a Rectangle with the private attribute,
            width and height , they must be positive integer,
            validated by integer_validator"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
