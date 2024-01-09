#!/usr/bin/python3
"""Definition of a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """
        Return the JSON representation of a string object.
        Args:
            my_obj(obj): Class object to serialize
        Return:
            Serialized object
    """

    return json.dumps(my_obj)
