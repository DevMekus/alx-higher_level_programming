#!/usr/bin/python3
"""Definition of a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing a square Model."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the Square Model.

        Args:
            *args (ints): New attribute values.
                - First argument represents id attribute
                - Second argument represents size attribute
                - Third argument represents x attribute
                - Fourth argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        if args and len(args) != 0:
            start = 0
            for arg in args:
                if start == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif start == 1:
                    self.size = arg
                elif start == 2:
                    self.x = arg
                elif start == 3:
                    self.y = arg
                start += 1

        elif kwargs and len(kwargs) != 0:
            for o, p in kwargs.items():
                if o == "id":
                    if p is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = p
                elif o == "size":
                    self.size = p
                elif o == "x":
                    self.x = p
                elif o == "y":
                    self.y = p

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
