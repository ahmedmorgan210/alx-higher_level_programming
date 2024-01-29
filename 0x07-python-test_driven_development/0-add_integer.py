#!/usr/bin/python3
"""Creating a function that adds 2 integers"""


def add_integer(a, b=98):
    """a function that adds 2 integers\
        Returns an integer: the addition of a and b
    """

    if isinstance(a, int) or isinstance(a, float):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, int) or isinstance(b, float):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
