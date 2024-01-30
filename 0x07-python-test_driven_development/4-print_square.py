#!/usr/bin/python3
"""prin the square module"""


def print_square(size):
    """prin the square func"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(0, size):
        for c in range(0, size):
            if c != (size - 1):
                print("#", end="")
            else:
                print("#")
