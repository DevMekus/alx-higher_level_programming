#!/usr/bin/python3
"""A Class that defines a Rectangle"""


class Rectangle:
    """Class representation of a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Width of the Rectangle
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set properties for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
            Sets the width value of the rectangle
            Raise:
                Raises a TypeError if value is not integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set properties for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
            Sets the height value of the rectangle
            Raise:
                Raises a TypeError if value is not integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returning the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returning the perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
