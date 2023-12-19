#!/bin/python3

class Square:
    __size

    def __init__(self, size=0):
        self.size = self.size(size);

    def size(self):
        return self.size;

    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0 :
            raise ValueError("size must be >= 0")
        else:
            return value

    def area(self):
        return self.size ** 2
