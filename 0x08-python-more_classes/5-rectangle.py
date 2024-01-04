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
        if not type(value) is not int:
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
        if type(value) is not int:
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

    def __str__(self):
        """
        Printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for index in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if index != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """
            Return the string representation of the Rectangle Class/Instance.
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """
            Displays a Message on the Deconstruction of the Rectangle.
        """
        print("Bye rectangle...")
