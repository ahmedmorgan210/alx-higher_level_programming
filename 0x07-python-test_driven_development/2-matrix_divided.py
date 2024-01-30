#!/usr/bin/python3
"""this is amtrix div"""


def matrix_divided(matrix, div):
    """ Doc """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or (len(matrix) == 0) or\
            type(matrix[0]) is not list or (len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for c in row:
            if type(c) is not int and type(c) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            if item == float('inf') or item == -float('inf') or item != item:
                new_row.append(10.0)
            else:
                new_row.append(item)
        new_matrix.append(new_row)

    final_matrix = []
    for row in new_matrix:
        final_row = []
        for item in row:
            final_row.append(round(item / div, 2))
        final_matrix.append(final_row)

    return final_matrix
