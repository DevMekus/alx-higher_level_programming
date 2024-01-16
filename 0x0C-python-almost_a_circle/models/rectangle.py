#!/usr/bin/python3

"""Module For the Class Definition of a Rectangle"""

from models.base import Base


class Rectangle(Base):
    """ The Class Definition of a Rectangle Class
        Args:
            width(int): The width of the rectangle
            height(int): The height of the rectangle
            x(int): The x coordinate of the rectangle
            y(int): The y coordinate of the rectangle

        methods:
            update: This function overwrite the already existing attribute
            dictionary: That returns the dictionary of an instance

        Raises:
            TypeError: This is raised when any of the attribute is not integer
            ValueError: Raised when x or y is less than zero or weight or
                        height is less than or equal to zero
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing the Rectangle Class """
        
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
             raise ValueError("width must be > 0")            
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
             raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
             raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

        
    @property
    def width(self):
        """ Getter for Width """

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the Width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """ Getter for the Height"""

        return self.__height

    @width.setter
    def height(self, value):
        """ Setter for the Height Property"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ Getter for X """

        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the X """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ Getter for Y"""

        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for Y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """ Returns the Area of Rectangle instance"""

        return self.__width * self.__height

    def display(self):
        """Prints the Area of a Rectangle with a #"""

        if self.__width and self.__height and self.__x and self.__y == 0:
            print(end="")

        for i in range(self.__y):
            print()

        for j in range(self.__height):
            for k in range(self.__width):
                for l in range(self.__x):
                    print(" ", end="")
                print("#", end="")
            print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")
                

    def update(self, *args, **kwargs):
        """ Updating attributes methods

        Args:
            args(int): The integer arguments to update attribute with

        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']

            for attribute, value in zip(attributes, args):
                if hasattr(self, attribute):
                    setattr(self, attribute, value)

        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)


    def to_dictionary(self):
        """ Return the dictionary of an instance"""
        return {'id':self.id, 
               'width':self.__width, 
               'height': self.__height,
               'x': self.__x,
               'y':self.__y
            }