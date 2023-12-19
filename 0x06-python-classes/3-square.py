#!/usr/bin/python3
"""Square Class or Module"""

class Square:
    """Defining a square object."""

    def __init__(self, size=0):
        """Square Initialization.
        Args:
            size (int): Size of new square in int.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """current area of the square."""
        return (self.__size * self.__size)
