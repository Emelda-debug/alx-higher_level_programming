#!/usr/bin/python3
"""scripts that akes in a URL, sends a request to the URL and displays
he body of the response (decoded in utf-8) """

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    """ takes in url, sends request and decodes """
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))

