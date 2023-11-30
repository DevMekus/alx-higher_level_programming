#!/usr/bin/python3.8
import hidden_4

if __name__ == "__main__":
    sorted_names = sorted((dir(hidden_4)))
    for name in sorted_names:
        if not name.startswith("__"):
            print(name)
