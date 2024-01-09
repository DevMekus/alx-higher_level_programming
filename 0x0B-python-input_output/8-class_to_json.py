#!/usr/bin/python3
"""Definition of a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Dictionary representation of a simple data structure.
    Args:
        obj(class): Object to change to get its dictionary
    """

    return obj.__dict_
