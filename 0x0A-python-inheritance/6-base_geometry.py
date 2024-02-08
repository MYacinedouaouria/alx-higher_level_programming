#!/usr/bin/python3
""" this module contain only on empty class called BaseGeometry"""


class BaseGeometry:
    """ defines a BaseGeometry class
        Public instance method:

        def area(self):
        raises an Exception with the message area() is not implemented
    """

    def area(self):
        """ raise an Exception with a message"""

        raise Exception('area() is not implemented')
