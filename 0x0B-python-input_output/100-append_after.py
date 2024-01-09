#!/usr/bin/python3
"""Definition of a new_text-file-insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert new_text after each line containing a given string in a file.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for within the file.
        new_string (str): String to insert.
    """
    new_text = ""
    
    with open(filename) as r:
        for line in r:
            new_text += line
            if search_string in line:
                new_text += new_string
                
    with open(filename, "w") as w:
        w.write(new_text)
