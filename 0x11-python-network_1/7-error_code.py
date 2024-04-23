#!/usr/bin/python3
"""scripts thattakes in a URL, sends a request to the URL and displays
response bpdy"""
import requests
import sys

if __name__ == "__main__":
    """ post data to webserver """
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
