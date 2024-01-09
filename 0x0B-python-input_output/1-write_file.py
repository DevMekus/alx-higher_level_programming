#!/usr/bin/python3
"""Definition of a file-writing function"""


def write_file(filename="", text=""):
    """Write a string to a text file.

    Args:
        filename (str): The file name to be written to.
        text (str): The text to write to the file.
    Returns:
        Returns The number of characters written.
    """
    
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
