#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

try:
    r = Rectangle(3, 5)
    print(r.height)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))