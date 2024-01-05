#!/usr/bin/python3
"""Class that define a Locked Class"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes    
    """

    __slots__ = ["first_name"]
