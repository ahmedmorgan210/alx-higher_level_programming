#!/usr/bin/python3
"""Square the number. """


class Square:
    """Define a square class. """

    def __init__(self, size=0):
        """
        Parameters
        ----------
            size : the size of the square.

        """
        try:
            self.__size = size
            if isinstance(size, int) and int(size) >= 0:
                #self.__size = size
                pass

        except TypeError:
            print("size must be an integer")

        except ValueError:
            print("size must be >= 0")
