#!/usr/bin/python3
"""A function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an existing object.

    Args:
        obj (any): object to add an attribute.
        att (str): Name of the attribute to add.
        value (any): The value of attribute to add.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
