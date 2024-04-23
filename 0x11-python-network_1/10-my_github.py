#!/usr/bin/python3
"""scripts that takes my 
GitHub credentials (username and password) and uses the GitHub API to displays id
"""
import requests
from sys import argv

if __name__ == "__main__":
    """ takes my github credentials """
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    req = = requests.get(url, auth=(username, password))\
            try:
                print(r.json().get('id'))
            except:
                pass
