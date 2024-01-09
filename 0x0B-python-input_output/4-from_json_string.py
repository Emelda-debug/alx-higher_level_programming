#!/usr/bin/python3
# 6-from_json_string.py
""" Returns an object (Python data structure) represented by a JSON string"""
import json

def from_json_string(my_str):
    """ Returns the JSON representation of a python object """
    return json.loads(my_str)
