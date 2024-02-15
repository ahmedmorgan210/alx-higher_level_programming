#!/usr/bin/python3
"""the rectangle module"""
from models.base import Base


class Rectangle(Base):
    """the rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """rectanglr attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """claculating the instance area"""
        return self.__width * self.__height

    def display(self):
        """display symbole"""
        for vertical in range(self.__y):
            print()
        for symbole in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self) -> str:
        return f"[Rectangle] " + \
            f"({self.id}) {self.__x}/{self.__y} " + \
            f"- {self.__width}/{self.__height}"

    def update(self, *args):
        """specify the arguments"""
        args_list = list(args)
        new_args = []
        if len(args) == 4:
            new_args.append(self.id)
            for item in args:
                new_args.append(item)

        elif len(args) == 1:
            self.id = args[0]
        else:
            new_args.append(args[4])
            for i in range(4):
                new_args.append[args[i]]

        #new_tuple = tuple(new_args)
                
        new_args.append() = self.id

        self.id = new_args[0]
        self.__width = new_args[1]
        self.__height = new_args[2]
        self.__x = new_args[3]
        self.__y = new_args[4]



        
        
        # if len(args) == 0:
        #     args[0] = self.id

        # if len(args) > 0:
        #     if len(args) >  1:
        #         args_list[0] = id
        #         args_list[1] = self.__width

        #     if len(args) >  2:
        #         args_list[0] = id
        #         args_list[1] = self.__width
        #         args_list[2] = self.__height

        #     if len(args) >  3:
        #         args_list[0] = id
        #         args_list[1] = self.__width
        #         args_list[2] = self.__height
        #         args_list[3] = self.__x

        # args_list[0] = self.id
        # args_list[1] = self.__width
        # args_list[2] = self.__height
        # args_list[3] = self.__x
        # args_list[4] = self.__y

        # args_tuple = tuple(args_list)


        # if len(args) >= 0:
        #     if len(args) == 0:
        #         args[0] = self.id
        #     if len(args) >= 1:

        #         args[0] = self.id
        #         args[1] = self.__width
        # else:
        #     pass
