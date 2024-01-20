#!/usr/bin/python3
"""a function that prints a dictionary by ordered keys\
        Keys should be sorted by alphabetic order
        You can assume that all keys are strings
        Only sort keys of the first level\
            (don’t sort keys of a dictionary inside the main dictionary)
        Dictionary values can have any type
        You are not allowed to import any module
"""


def print_sorted_dictionary(a_dictionary):
    new_dict = {}
    dir_list = list(a_dictionary)
    dir_list.sort()
    for i in dir_list:
        new_dict[i] = a_dictionary[i]
        print(f"{i}: {new_dict[i]}")
