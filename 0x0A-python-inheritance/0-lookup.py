#!/usr/bin/python3
"""
   this module suplies one function, lookup(obj)
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    Args:
        obj: the object to inspect.
    """

    return dir(obj)
