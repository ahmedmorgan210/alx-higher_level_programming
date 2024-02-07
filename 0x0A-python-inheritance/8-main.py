#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry

r = Rectangle(3, 5)
print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

print("Rectangle:", Rectangle)
print("BaseGeometry:", BaseGeometry)
print("Is Rectangle a subclass of BaseGeometry?", issubclass(Rectangle, BaseGeometry))