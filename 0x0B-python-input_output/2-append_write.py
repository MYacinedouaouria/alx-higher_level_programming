#!/usr/bin/python3
""" this module suplies one functio, append_write()"""


def append_write(filename="", text=""):
    """ this function append a string at the end of a textfile (UTF8)
        and returns the number of characters added"""

    with open(filename, "a", encoding="utf-8") as a_file:
        pos_bf = a_file.tell()
        a_file.write(text)
        nb = a_file.tell() - pos_bf
    return nb
