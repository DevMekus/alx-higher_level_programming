#!/usr/bin/python3

"""Definition of a JSON-to-object function."""

import json


def from_json_string(my_str):
    """
        Python object representation of a JSON string.
        Args:
            my_str(str): String to pass to the function
        Return:
            Deserialized String
    """

    return json.loads(my_str)
