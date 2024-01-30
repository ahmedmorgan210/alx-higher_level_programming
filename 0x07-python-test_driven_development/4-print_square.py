#!/usr/bin/python3
"""prin the square module"""


def print_square(size):
    """prin the square func"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    for r in range(0, size):
        for c in range(0, size):
            if c != (size - 1):
                print("#", end="")
            else:
                print("#")
