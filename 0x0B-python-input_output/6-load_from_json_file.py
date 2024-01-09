#!/usr/bin/python3
"""Definition a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.
    Args:
        filename(str): The name of file to deserialize from
    Return:
        A Python Object
    """

    with open(filename) as fil:
        return json.load(fil)
