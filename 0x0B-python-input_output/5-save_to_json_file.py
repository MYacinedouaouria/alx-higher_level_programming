#!/usr/bin/python3
"""this module suplies one function, save_to_json_file()"""


import json


def save_to_json_file(my_obj, filename):
    """ this function writes an Object to a text file,
        using a JSON representation"""

    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
