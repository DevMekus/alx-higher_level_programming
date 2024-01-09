#!/usr/bin/python3
"""Definition of a text-file-reading function."""


def read_file(filename=""):
    """Prints a UTF8 text file content"""
    
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
