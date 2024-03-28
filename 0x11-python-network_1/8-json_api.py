#!/usr/bin/python3
"""scripts that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter
as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    """ sendind data to webserver """
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
        qry= {'q': q}
        response = requests.post(url, data=qry)
        if response.status_code != requests.codes.ok or len(response.text) <= 0:
            print('No result')
            sys.exit()

        else:
            try:
                obj = response.json()
                if len(obj)== 0:
                    print('No result')
                     sys.exit()
                     my_id = obj.get('id')
                     my_name = obj.get('name')
                     print("[{}] {}".format(my_id, my_name))
            except ValueError as invalid_json:

                print('Not a valid JSON')

