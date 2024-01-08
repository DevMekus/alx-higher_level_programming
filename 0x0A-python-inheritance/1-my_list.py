#!/bin/python3
"""Class Definition of an inherited list class MyList."""


class MyList(list):
    """Sorted Algorithm for a buil-in list class"""

    def print_sorted(self):
        """Sorts the built in List Class"""
        print(sorted(self))
