#!/usr/bin/python3
"""
Sending a POST request to the passed URL with the email as a parameter,
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    args = sys.argv
    url = args[1]
    email = args[2]
    DATA = urllib.parse.urlencode({"email": email})
    DATA = DATA.encode('ascii')

    with urllib.request.urlopen(url, DATA) as response:
        print(response.read().decode('utf-8'))