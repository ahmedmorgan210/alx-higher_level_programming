#!/usr/bin/python3
"""the inhereted square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        print(f"Size type: {type(size)}")
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        # return f"[Square] " + \
        #     f"({self.id}) {self.x}/{self.y} " + \
        #     f"- {self.size}"
