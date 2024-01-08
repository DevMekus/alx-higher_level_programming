#!/usr/bin/python3
"""Definition of an empty class BaseGeometry."""


class BaseGeometry:
    """Base Geometry class."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if param is an Integer.

        Args:
            name (str): Parameter name.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
