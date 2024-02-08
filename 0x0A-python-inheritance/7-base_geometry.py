#!/usr/bin/python3
""" this module contain only on empty class called BaseGeometry"""


class BaseGeometry:
    """ defines a BaseGeometry class
        Public instance method:

        def area(self):
        raises an Exception with the message area() is not implementedi
        def integer_validator(self, name, value):
        validates value
    """

    def area(self):
        """ raise an Exception with a message"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
           this function validates a value, the value have to be an integer:
           - if value is not an integer: raise a TypeError exception,
           with the message <name> must be an integer
           - if value is less or equal to 0: raise a ValueError exception
           with the message <name> must be greater than 0
           name: is always a string
        """

        if (type(value) is int):
            if (value <= 0):
                raise ValueError(f'{name} must be greater than 0')
        else:
            raise TypeError(f'{name} must be an integer')
