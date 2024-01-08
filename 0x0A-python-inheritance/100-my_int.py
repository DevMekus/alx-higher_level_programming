#!/usr/bin/python3
"""Modeling a class MyInt that inherits from int."""


class MyInt(int):
    """Methods that Invert int operators == and !=."""

    def __eq__(self, value):
        """Override ==  with != ."""
        return self.real != value

    def __ne__(self, value):
        """Override != with == ."""
        return self.real == value
