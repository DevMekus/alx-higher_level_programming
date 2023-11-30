#!/usr/bin/python3.8
import hidden_4

if __name__ == "__main__":
       sorted_name = sorted(name for name in dir(hidden_4) if not name.startswith("__"))
       for the_name in sorted_name:
           print(the_name)
