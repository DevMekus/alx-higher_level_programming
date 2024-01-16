#!/usr/bin/python3

"""Module For the Class Definition of a Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ 
    The Class Definition of a Square Class
        Args:
            size(int): The size of the square
            id(int): The id of the square
            x(int): The x coordinate of the rectangle
            y(int): The y coordinate of the rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the String value of the object"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    @property
    def size(self):
        """Getter for the Size"""

        return self.width

    @size.setter
    def size(self, size):
        """Setter for the Size"""

        self.width = size

    def update(self, *args, **kwargs):
        """ Updating attributes methods

        Args:
            args(int): The integer argument to update attribute with

        """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for attr, value in zip(attrs, args):
                if hasattr(self, attr):
                    setattr(self, attr, value)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }