#!/usr/bin/python3
"""this module suplies one function, load_from_json_file()"""


import json


def load_from_json_file(filename):
    """ this function creates an object from a JSON file"""

    with open(filename, encoding="utf-8") as a_file:
        obj = json.load(a_file)
    return obj
