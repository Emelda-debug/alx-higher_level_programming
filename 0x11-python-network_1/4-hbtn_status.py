#!/usr/bin/python3
"""scripts that etches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print_str = '''Body response:
\t- type: {}
\t- content: {}'''.format(type(content), content)
print(print_str)

