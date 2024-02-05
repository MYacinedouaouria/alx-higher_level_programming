#!/usr/bin/python3
"""
   this module define the class MyList
"""


class MyList(list):
    """
       this class inherit from the list class
       methods: print_sorted(self)  prints the list but in sorted order
    """

    def print_sorted(self):
        """ this function get a MyList object from parameter,
            then copy it and then make the copy sorted,
            then prints the copy """

        copy = self[:]
        copy.sort()
        print(copy)
