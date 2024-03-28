#!/usr/bin/python3
"""scripts that  fetches https://alx-intranet.hbtn.io/status """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        html_str = html.decode('utf-8')

    print('- Body response:)
    print('\t', body)
