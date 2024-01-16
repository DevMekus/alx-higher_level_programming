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
        """Print the Rectangle using the `#` character."""

        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y_cord in range(self.y)]
        for h_cord in range(self.height):
            [print(" ", end="") for x_cord in range(self.x)]
            [print("#", end="") for w_cord in range(self.width)]
            print("")


    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")
                

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
        """ Return the dictionary of an instance"""
        return {'id':self.id, 
               'width':self.__width, 
               'height': self.__height,
               'x': self.__x,
               'y':self.__y
            }