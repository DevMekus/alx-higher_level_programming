#!/usr/bin/python3
"""Definition of a Rectangle Class"""
from models.base import Base


class Rectangle(Base):
    """Modelling a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): x coordinate of the new Rectangle.
            y (int): y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            ValueError: If either of width or height <= 0.
            TypeError: If either of width or height is not an int.
            ValueError: If either of x or y < 0.
            TypeError: If either of x or y is not an int.
           
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    
    @property
    def width(self):
        """gets the width of the Rectangle."""
        
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate of the Rectangle."""

        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the Rectangle."""

        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""

        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""

        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y_cord in range(self.y)]
        for h_cord in range(self.height):
            [print(" ", end="") for x_cord in range(self.x)]
            [print("#", end="") for w_cord in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle Model.

        Args:
            *args (ints): New attribute values.
                - First argument is id attribute
                - Second argument is width attribute
                - Third argument is height attribute
                - Fourth argument is x attribute
                - Fifth argument is y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            start = 0
            for arg in args:
                if start == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif start == 1:
                    self.width = arg
                elif start == 2:
                    self.height = arg
                elif start == 3:
                    self.x = arg
                elif start == 4:
                    self.y = arg
                start += 1

        elif kwargs and len(kwargs) != 0:
            for o, p in kwargs.items():
                if o == "id":
                    if p is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = p
                elif o == "width":
                    self.width = p
                elif o == "height":
                    self.height = p
                elif o == "x":
                    self.x = p
                elif o == "y":
                    self.y = p

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
