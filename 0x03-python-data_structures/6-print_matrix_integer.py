#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        print()
    else:
        for row in matrix:
            for i in range(len(row) - 1):
                print("{:d}".format(row[i]), end=" ")
            print(row[-1])
