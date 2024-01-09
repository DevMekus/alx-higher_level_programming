#!/usr/bin/python3
"""Definition of a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.
    Args:
        my_obj(obj): Object to be written to a file
        filename(str): The name of file to write to
    """

    with open(filename, "w") as fil:
        json.dump(my_obj, fil)
