#!/usr/bin/python3
"""
   this is the "2-matrix_divided" module
   this module suplies on function, matrix_divided()
   Prototype: def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """ divides all elements of a matrix
        matrix must be a list of lists of integers or floats
        each row must be the same size and div must be a number != 0"""

    str1 = "matrix must be a matrix (list of lists) of integers/floats"
    str2 = "Each row of the matrix must have the same size"
    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if isinstance(matrix, list):
        if all(isinstance(sublist, list) for sublist in matrix):
            if all(isinstance(e, (int, float)) for row in matrix for e in row):
                lenght = len(matrix[0])
                if all(len(sub_list) == lenght for sub_list in matrix):
                    result = []
                    for row in matrix:
                        new_row = []
                        for element in row:
                            new_row.append(round(element / div, 2))
                        result.append(new_row)
                    return result
                else:
                    raise TypeError(str2)
            else:
                raise TypeError(str1)
        else:
            raise TypeError(str1)
    else:
        raise TypeError(str1)
