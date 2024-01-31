#!/usr/bin/python3
"""
   this is the module '5-text_indentation'
   this module suply one function , 'text_indentation'
   that prints a text with 2 new lines after each of these characters: .? and :
"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters: .? and :
        text must be a string, otherwise raise a TypeError exception
        There should be no space at the beginning or at the end of each line"""

    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    new_line = True
    for i in range(len(text)):
        if (text[i] == " " and new_line):
            continue
        elif (text[i] in ".?:"):
            print(text[i])
            print()
            new_line = True
        else:
            print(text[i], end="")
            new_line = False
