#!/usr/bin/python3
"""Definition of a Class Checking Function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly 
    an instance of a given class.

    Args:
        obj (any): Provided Object to check.
        a_class (type): The class to reference with.
    Returns:
        True: If obj is exactly an instance of a_class 
        Else - False.
    """

    if type(obj) == a_class:
        return True
    return False
