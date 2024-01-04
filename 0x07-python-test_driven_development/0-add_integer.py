#!/bin/python3

"""function that adds 2 integers."""

def add_integer(a, b=98):
    """
        add_integer is a function that adds two integers
        Args:
            a (int):  first integer to be provided 
            b (int): A second integer to be provided but defaulted to 98
        Return:
            The return (int) value is an addition of the two arguments
    """
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
