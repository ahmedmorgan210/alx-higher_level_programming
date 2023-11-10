#!/usr/bin/python3

def no_c(my_string):
    new_word = ""

    string = list(my_string)

    for i in range(len(string)):
        if string[i] == 'c' or string[i] == 'C':
            continue
        else:
            new_word += string[i]

    return new_word
