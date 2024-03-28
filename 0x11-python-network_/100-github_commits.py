#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”

"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    repository = argv[1]
    owner = argv[2]
    i = 0

    URL = "https://api.github.com/repos/{}/{}/commits".format(owner, repository)

    response = get(URL)
    json = response.json()

    for item in json:
        if i > 9:
            break
        sha = item.get('sha')
        author = item.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        i += 1
