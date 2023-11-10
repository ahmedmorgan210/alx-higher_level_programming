#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    A function that prints a matrix of integers\
            You are not allowed to import any module
            You can assume that the list only contains integers
            You are not allowed to cast integers into strings
            You have to use str.format() to print integers
    """
    if len(matrix) <= 0:
        exit(-1)
    else:

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j < len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][j]), end=' ')

                else:
                    print("{:d}".format(matrix[i][j]))
