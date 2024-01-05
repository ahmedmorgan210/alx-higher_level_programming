#!/usr/bin/python3

"""
program that prints the ASCII alphabet, in reverse order,\
        alternating lowercase and uppercase
        (z in lowercase and Y in uppercase)
        - You can only use one print function with string format
        - You can only use one loop in your code
        - You are not allowed to store characters in a variable
        - You are not allowed to import any module
"""

for letter in range(ord('z'), ord('a')-1, -1):

    if letter % 2:
        new_letter = letter - 32
    else:
        new_letter = letter
    print("{}".format(chr(new_letter)), end="")
