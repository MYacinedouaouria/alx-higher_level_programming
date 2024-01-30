#!/usr/bin/python3
"""
   this is the "3-say_my_name" module
   this module suplies on function , say_my_name()
   Prototype: def say_my_name(first_name, last_name=""):
"""


def say_my_name(first_name, last_name=""):
    """  prints My name is <first name> <last name>
         first_name and last_name must be strings otherwise,
         raise a TypeError exception with a message """

    if (isinstance(first_name, str) and isinstance(last_name, str)):
        print(f"My name is {first_name} {last_name}")
    elif (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    else:
        raise TypeError("last_name must be a string")
