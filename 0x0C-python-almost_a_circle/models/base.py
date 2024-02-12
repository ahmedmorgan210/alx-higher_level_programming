#!/usr/bin/python3
""" the base class"""


class Base:
    """the base of all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """manage id attribute in all your future classes\
            and to avoid duplicating the same code
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
