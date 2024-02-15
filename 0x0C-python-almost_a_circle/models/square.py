#!/usr/bin/python3
"""the inhereted square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square chape class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing thw square"""
        print(f"Size type: {type(size)}")
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ method of the reqtangle parent class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        # return f"[Square] " + \
        #     f"({self.id}) {self.x}/{self.y} " + \
        #     f"- {self.size}"
