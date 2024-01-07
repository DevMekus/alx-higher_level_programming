#!/usr/bin/python3

"""Integer Addition Function."""


def add_integer(a, b=98):
    """
    Returns the addition of a and b.
    Type Caste Float arguments before operation.
    Args:
        a (int): First Integer
        b (it): Second Integer
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
