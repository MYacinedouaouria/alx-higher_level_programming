#!/usr/bin/env python3
# defines a function that returns a key with the biggest integer value

def best_score(a_dictionary):
    """" this function looks for the biggest value and return the key"""

    maxi = 0
    best_key = ''
    if (a_dictionary is None):
        return None
    for key, value in a_dictionary.items():
        if value > maxi:
            best_key = key
            maxi = a_dictionary[key]
    return best_key
