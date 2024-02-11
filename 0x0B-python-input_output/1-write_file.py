#!/usr/bin/python3
""" this module suplies one function, write_file()"""


def write_file(filename="", text=""):
    """ this function writes a string to a text file (UTF8)
        and returns the number of characters written"""

    with open(filename, "w", encoding="utf-8") as file_name:
        file_name.write(text)
        position = file_name.tell()
    return position
