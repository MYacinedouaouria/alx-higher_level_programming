#!/usr/bin/python3
"""
   this is the '4-print_square' module
   this module suplies on function , print_square()
   prototype def print_square(size):
"""


def print_square(size):
    """prints a square with the character #
       size is the size of the square , and it must be an integer otherwise
       raise a TypeError exception , and >= 0 otherwise raise a ValueError"""

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    else:
        if (size == 0):
            print()
        for i in range(size):
            for j in range(size - 1):
                print("#", end="")
            print("#")
