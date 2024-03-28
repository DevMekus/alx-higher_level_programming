#!/usr/bin/python3
import sys
import urllib.request
"""
Displays the value of the X-Request-Id variable
"""

if __name__ == "__main__":  

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])