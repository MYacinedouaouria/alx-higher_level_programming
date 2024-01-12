#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = sorted(a_dictionary)
    for k in s:
        print("{0:s}: {1}".format(k, a_dictionary[k]))
