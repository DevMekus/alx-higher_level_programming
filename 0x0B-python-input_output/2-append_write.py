#!/usr/bin/python3
"""Definition of a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a file.

    Args:
        filename (str): Name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
