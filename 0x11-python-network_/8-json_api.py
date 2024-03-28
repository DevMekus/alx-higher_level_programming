#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    response = post(URL, data)

    resType = response.headers['content-type']

    if resType == 'application/json':
        resResult = response.json()
        _id = resResult.get('id')
        name = resResult.get('name')
        if (resResult != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
