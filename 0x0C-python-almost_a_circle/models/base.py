#!/usr/bin/python3
""" creating class BASE """
import json
import csv
import turtle

class Base:
""" class Base with private class attribute  __nb_objects = 0 and class constructor def __init__(self, id=None)"""
__nb_objects = 0
def __init__(self, id=None):
    """ Initialise a new Base
    Args:
    id: int base ID
    """
    if id is not None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects

@staticmethod
def to_json_string(list_dictionaries):
    """ returns the JSON string representation of list_dictionaries:
    Args:
    list_dictionaries: is a list of dictionaries
    """
    if list_dictionaries is None or list_dictionaries == []:
        return "[]"
    return json.dumps(list_dictionaries)

@classmethod
def save_to_file(cls, list_objs):
    """  writes the JSON string representation of list_objs to a file:
    Args:
    list_objs:  list of instances who inherits of Base
    """
    filename = cls.__name__ + ".json"
    with open(filename, "w") as jsonfile:
        if list_objs is None:
            jsonfile.write("[]")

        else:
            list_dicts = [o.to_dictionary() for o in list_objs]
            jsonfile.write(Base.to_json_string(list_dicts))

@staticmethod
def from_json_string(json_string):
    """ returns the list of the JSON string representation json_string
    Args:
    json_string: is a string representing a list of dictionaries
    """
    if json_string is None:
        return []
    return json.loads(json_string)

@classmethod
def create(cls, **dictionary):
    """ returns an instance with all attributes already set:
    Args:
    ** dictionary: double pointer to a dictionary
    """
    if dictionary and dictionary != {}:

