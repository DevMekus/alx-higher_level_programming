#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if (len(sys.argv[1:]) < 1):
        print(f"{len(sys.argv[1:])} arguments:")
    else:
        print(f"{len(sys.argv[1:])} arguments:")
        for i in sys.argv[1:]:
            print(f"{sys.argv.index(i)}: {i}")
