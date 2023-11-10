#!/usr/bin/python3

def no_c(my_string):
    """
    A function that removes all characters c and C from a string\
            The function should return the new string
            You are not allowed to import any module
            You are not allowed to use str.replace()
    """
    new_word = ""

    string = list(my_string)

    for i in range(len(string)):
        if string[i] == 'c' or string[i] == 'C':
            continue
        else:
            new_word += string[i]

    return new_word
