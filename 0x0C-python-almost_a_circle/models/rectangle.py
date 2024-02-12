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

        self.__width = width

    @height.setter
    def height(self, height):
        """sets the height"""

        self.__height = height

    @x.setter
    def x(self, x):
        """sets the x attribute"""

        self.__x = x

    @y.setter
    def y(self, y):
        """sets the attribute y"""

        self.__y = y
