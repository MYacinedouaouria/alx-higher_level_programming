#!/usr/bin/python3
""" this is a script that adds all arguments to a python list,
    and save them to a file"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
arguments = sys.argv[:]
try:
    lis_t = load_from_json_file("add_item.json")
except FileNotFoundError:
    lis_t = []

if (len(arguments) == 1):
    save_to_json_file(lis_t, "add_item.json")
else:
    for element in arguments[1:]:
        lis_t.append(element)
    save_to_json_file(lis_t, "add_item.json")
