#!/usr/bin/python3
for index in range(122, 96, -1):
    if index % 2:
        index = index - 32
    print("{:c}".format(index), end="")
