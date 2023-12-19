#!/usr/bin/python3

class Square:
    __size

    def __init__(self, size=0):
        if type(size) is not int:
            raise raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size

    def area(self):
        return self.size ** 2
