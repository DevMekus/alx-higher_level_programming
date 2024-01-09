#!/bin/python3
"""Class Definition of an inherited list class MyList """

class MyList(list):
    """Sorted Algorithm for a buil-in list class"""

    def __init__(self, *args, **argss):
        """ Call the constructor of the base class (list)"""

        super().__init__(*args, **argss)

    def print_sorted(self):
        """Printing the List in a sorted form """

        sorted_list = sorted(self)
        print(sorted_list)
