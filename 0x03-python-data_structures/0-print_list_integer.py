#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    a function that prints all integers of a list\
            Format: one integer per line.
            You are not allowed to import any module
            You can assume that the list only contains integers
            You are not allowed to cast integers into strings
            You have to use str.format() to print integers

    """
    for num in range(len(my_list)):
        print("{:d}".format(my_list[num]))
