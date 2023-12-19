#!/usr/bin/python3
"""Defining a Square Class or Module"""


class Square:
    """Defining a Square Object"""

    def __init__(self, size=0):
        """Init Square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter for the  size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """current area of the square."""
        return (self.__size * self.__size)
