#!/usr/bin/python3
"""prin the square module"""


def print_square(size):
    """prin the square func"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("Fail")
