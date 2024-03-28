#!/usr/bin/python3
"""
Sending a request to the URL and displays the body of the response
"""


if __name__ == '__main__':
    import sys
    from urllib import request, error

    args = sys.argv
    url = args[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.status))
