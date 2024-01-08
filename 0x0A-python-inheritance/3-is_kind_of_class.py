#!/usr/bin/python3
"""Definition of an Inheritance Checking Function."""

def is_kind_of_class(obj, a_class):
    """considers if an object 
    is an instance of a class.

    Args:
        obj (any): Considering Object.
        a_class (type): Inherited Class.
    Returns:
         True: If obj is an instance of a_class 
        Else - False.
    """

    if isinstance(obj, a_class):
        return True
    return False
