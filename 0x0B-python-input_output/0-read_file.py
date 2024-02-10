#!/usr/bin/python3
"""this module suplies one function, read_fite"""


def read_file(filename=""):
    """ this function reads a text file and prints it to stdout"""

    with open(filename, encoding="utf-8") as a_file:
        print (a_file.read(), end="")
