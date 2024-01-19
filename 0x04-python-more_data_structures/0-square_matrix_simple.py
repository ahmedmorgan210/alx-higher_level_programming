#!/usr/bin/python3

"""a function that computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    new_list = []
    for i in range(len(matrix)):
        sub_list = []
        for j in matrix[i]:
            x = j**2
            sub_list.append(x)

        new_list.append(sub_list)

    return new_list
