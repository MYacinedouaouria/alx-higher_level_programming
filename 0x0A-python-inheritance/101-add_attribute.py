#!/usr/bin/python3
""" this module suplies one function add_attribute"""


def add_attribute(obj, name, value):
    """ checks if obj has already an attribute caled name ,
        if there is an attribute then raise exceprion
        otherwise add that atribute"""

    if not isinstance(obj, (int, float, str, tuple, frozenset)):
        if (not hasattr(obj, name)):
            setattr(obj, name, value)
        else:
            raise TypeError("can't add new attribute")
    else:
        raise TypeError("can't add new attribute")
