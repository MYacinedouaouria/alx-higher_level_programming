#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    new_list = my_list
    for i in range(len(new_list)):
        print("{:d}".format(new_list[i]))
