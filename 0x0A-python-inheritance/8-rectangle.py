#!/usr/bin/python3
"""rectangle mod"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle from base"""
    def __init__(self, width, height):
        """init func"""
        # self.height = self.integer_validator("height", height)
        # self._width = width
        if self.integer_validator("height", height)and\
              self.integer_validator("width", width):  
        # if self.integer_validator("width", width) and\
        #         self.integer_validator("height", height):
            self._width = width
            self.height = height

        # if self.integer_validator("width", width):
        #     self._width = width

        # if self.integer_validator("height", height):
        #     self.height = height
        # self._width = self.integer_validator("width", width)
        # self.height = self.integer_validator("height", height)
        # self.height = height

        # self.height = height
        # self.integer_validator("height", height)
    # @property
    # def get_height(self):
    #     """getting height"""
    #     return (self.height)
# print(dir(Rectangle))
