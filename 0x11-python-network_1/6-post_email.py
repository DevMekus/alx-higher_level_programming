#!/usr/bin/python3
"""
Sending a POST request to the passed URL with the email as a parameter"""


if __name__ == '__main__':
    from sys import argv
    from requests import post

    urls = argv[1]
    email = argv[2]
    res = post(urls, {'email': email})
    print(res.text)