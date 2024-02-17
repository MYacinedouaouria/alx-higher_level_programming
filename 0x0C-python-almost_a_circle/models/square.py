#!/usr/bin/python3
""" this module defines the class Square that inherit from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherits from Rectangle
        Class constructor: def __init__(self, size, x=0, y=0, id=None):
        the constructor of a Rectangle
        overloading __str__ method: returns a string description of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a square by the mondatory size and x and y an id"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ returns the size of the Square"""

        return self.width

    @size.setter
    def size(self, size):
        """sets the size of a square"""

        if isinstance(size, int):
            if (size <= 0):
                raise ValueError("width must be > 0")
            else:
                self.width = size
                self.height = size
        else:
            raise TypeError("width must be an integer")

    def update(self, *args, **kwargs):
        """asigns attributes"""

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if (hasattr(self, key)):
                    setattr(self, key, value)
