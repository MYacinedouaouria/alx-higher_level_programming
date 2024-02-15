#!/usr/bin/python3
""" this module defines class Rectangle that inherits from Base """


from .base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base:
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes a Rectangle """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ returns the area of a rectangle"""

        return self.width * self.height

    @property
    def width(self):
        """retrives the width of the Rectangle"""

        return self.__width

    @property
    def height(self):
        """retrives the height of the Rectangle"""

        return self.__height

    @property
    def x(self):
        """retrives the x attribute of the Rectangle"""

        return self.__x

    @property
    def y(self):
        """ retrves the y attribute of a Rectangle"""

        return self.__y

    @width.setter
    def width(self, width):
        """ sets the width"""

        if isinstance(width, int):
            if (width <= 0):
                raise ValueError("width must be > 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, height):
        """sets the height"""

        if isinstance(height, int):
            if (height <= 0):
                raise ValueError("height must be > 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")

    @x.setter
    def x(self, x):
        """sets the x attribute"""

        if (isinstance(x, int)):
            if (x < 0):
                raise ValueError("x must be >= 0")
            else:
                self.__x = x
        else:
            raise TypeError("x must be an integer")

    @y.setter
    def y(self, y):
        """sets the attribute y"""

        if (isinstance(y, int)):
            if (y < 0):
                raise ValueError("y must be >= 0")
            else:
                self.__y = y
        else:
            raise TypeError("y must be an integer")
