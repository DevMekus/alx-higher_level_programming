#!/usr/bin/python3
import sys
import math

if __name__ == "__main__":
    result = 0
    arguments =sys.argv[1:]
    for i in arguments:
        result += int(i)
    print("{}".format(result))
