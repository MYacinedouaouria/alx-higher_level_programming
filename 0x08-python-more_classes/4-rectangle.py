#!/usr/bin/python3
"""
   this is the 4-rectangle module
   contain definition of the class Rectangle , a real definition of a rectangle

"""


class Rectangle:
    """ a class representing a Rectangle object
        Atributes:
            width: have to be an integer and >= to 0
            height: have to be an integer and >= to 0
            area(): returns the rectangle area
            perimeter(): returns the rectangle perimeter
    """

    def __init__(self, width=0, height=0):
        """ initialize a Rectangle object with given attributes"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """ returns the attribute width of the object"""

        return self.__width

    @property
    def height(self):
        """ returns the attribute height of the instance"""

        return self.__height

    @width.setter
    def width(self, width):
        """ sets the width of the rectangle
            must be an integer otherwise raise TypeError exception with mesage
            must be >= 0 otherwise raise ValueError exception with message"""

        if (isinstance(width, int)):
            if (width < 0):
                raise ValueError("width must be >= 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, height):
        """ sets the height of the rectangle
            must be an integer otherwise raise TypeError exception with message
            must be >= 0 otherwise raise ValueError exception with message"""

        if (isinstance(height, int)):
            if (height < 0):
                raise ValueError("height must be >= 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """  returns the rectangle area """

        return self.width * self.height

    def perimeter(self):
        """ returns the rectangle perimeter"""

        if (self.width == 0 or self.height == 0):
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ returns a string : the rectangle with the character #"""

        r = ""
        if (self.width == 0 or self.height == 0):
            return r
        for i in range(self.height - 1):
            for j in range(self.width):
                r += "#"
            r += "\n"
        for k in range(self.width):
            r += "#"
        return r

    def __repr__(self):
        """ returns a string representation of the rectangle"""

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
