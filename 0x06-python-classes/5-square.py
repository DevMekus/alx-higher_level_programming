#!/usr/bin/python3
"""Defining a Square class or module"""

class Square:
    """Building the square model with class"""

    def __init__(self, size):
        """Initialization of  a new square.
        Args:
            size (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Getter for the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with a symbol"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")       
