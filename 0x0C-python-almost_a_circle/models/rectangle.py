#!/usr/bin/python3
"""the rectangle module"""
from models.base import Base


class Rectangle(Base):
    """the rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """rectanglr attributes"""
        super().__init__(id)
        # self.__width = width
        if type(self.width) is not int:
            raise TypeError("width must be an integer")
        if self.width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width       
        self.__height = height
        if type(self.height) is not int:
            raise TypeError("height must be an integer")
        if self.height <= 0:
            raise ValueError("height must be > 0")
        # self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        if type(self.height) is not int:
            raise TypeError("height must be an integer")
        if self.height <= 0:
            raise ValueError("height must be > 0")
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        if not isinstance(self.__x, int):
            raise TypeError("height must be an integer")
        if self.__x <= 0:
            raise ValueError("height must be > 0")
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
