#!/usr/bin/python3
"""
Function to Find Max Integer in a List
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list
       function returns None if list is empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return
