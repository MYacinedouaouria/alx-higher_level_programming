#!/usr/bin/python3
""" this module defines on class MyInt that inherit the int class"""


class MyInt(int):
    """ this class defines a class MyInt that inherits the int
        MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, other):
        """ when comparing 2 MyInt objects with '==',
            return true if the value is different, False oterwise"""

        return super().__ne__(other)

    def __ne__(self, other):
        """ when comparing 2 MyInt objects with '!=',
            return False if the value is different, true  oterwise"""

        return super().__eq__(other)
