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
