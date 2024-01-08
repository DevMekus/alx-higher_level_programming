#!/usr/bin/python3
"""Defines a function that looks up object attribute"""

def lookup(obj):
    """
        Returns a list of an object's available attributes.
        Args:
            obj (class): Object to looku for
        Return:
            Returns all the methods found in the object
    """

    return (dir(obj))
