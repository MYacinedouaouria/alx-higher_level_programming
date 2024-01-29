#!/usr/bin/python3
"""
this is the 0-add_integer module
the 0-add_integer module define 1 function , add_integer()

"""


def add_integer(a, b=98):
    """ Returns an integer: the addition of a and b
        a and b must be int or float, otherwise raise a TypeError exception
        a and b must be first casted to integers if they are float """

    if isinstance(a, (int, float)):
        if (isinstance(a, int)):
            n1 = a
        else:
            n1 = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        if (isinstance(b, int)):
            n2 = b
        else:
            n2 = int(b)
    else:
        raise TypeError("b must be an integer")
    return n1 + n2
