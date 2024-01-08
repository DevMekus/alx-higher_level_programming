#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Considers if an object is an inherited instance of a class.

   Args:
        obj (any): Considering Object.
        a_class (type): Inherited Class.
    Returns:
         True: If obj is an inherited instance of a_class 
        Else - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
