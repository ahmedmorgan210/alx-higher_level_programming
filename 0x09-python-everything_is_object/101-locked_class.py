#!/usr/bin/python3
"""lock class"""


class LockedClass:
    """lock class"""

    # def __new__(cls):
    #     obj = super().__new__(cls)
    #     return obj

    def __setattr__(self, name, value):
        if not isinstance(name, str):
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        if name != 'first_name':
            raise\
                AttributeError(f"'LockedClass' object has no attribute '{name}'")
        else:
            super().__setattr__(name, value)
