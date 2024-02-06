#!/usr/bin/python3
""" this module suply one function,
    def is_same_class(obj, a_class):"""


def is_same_class(obj, a_class):
    """ this function checks if an object obj is exactly an instance of a_class
        return True if it is an instance of a_class , otherwise return False"""

    return type(obj) is a_class
