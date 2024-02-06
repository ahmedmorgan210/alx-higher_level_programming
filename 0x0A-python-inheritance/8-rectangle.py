#!/usr/bin/python3
"""rectangle mod"""


class BaseGeometry:
    """new base geometry class"""
    # def __init__(self, name, value):
    #     self.name = name
    #     self.value = value

    def area(self):
        """rais exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value validator"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle from base"""
    def __init__(self, width, height):
        """init func"""
        self._width = self.integer_validator("width", width)
        self.height = self.integer_validator("height", height)
