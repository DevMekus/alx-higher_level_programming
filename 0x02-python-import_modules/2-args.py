#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    arg_len = len(arguments)

    if (arg_len < 1):
        print("0 arguments:")
    else:
        print(f"{arg_len} arguments:")
        for i in arguments:
            print(f"{sys.argv.index(i)}: {i} ")
            
    
