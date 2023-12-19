#!/usr/bin/python3
"""Square Class or Module"""


class Square:
    """Defining a Square Object"""

    def __init__(self, size=0):
        """new Square Initialize
        Args:
            size (int): Size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
