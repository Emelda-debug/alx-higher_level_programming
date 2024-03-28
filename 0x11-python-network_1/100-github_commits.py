#!/usr/bin/python3
"""scripts that takes 2 arguments in order to solve this challenge""
"""
import requests
from sys import argv

if __name__ == "__main__":
    """ lists 10 commits"""
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    reqs = requests.get(url)
    r_list = r.json()
    try:
        for x in range(10):
            print("{}: {}".format(r_list[x].get('sha'), r_list[x].
                get('commit').get('author').get('name'))

    except:
        pass

