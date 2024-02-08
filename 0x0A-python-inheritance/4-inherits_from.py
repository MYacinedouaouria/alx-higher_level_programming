#!/usr/bin/python3
"""
   this module suplies one function , inherits_from
"""


def inherits_from(obj, a_class):
    """
       returns True if the object is an instance of a class that inherited
       (directly or indirectly) from the specified class ; otherwise False.
    """

    return (isinstance(obj, a_class) and (type(obj) is not a_class))
