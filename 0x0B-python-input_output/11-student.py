#!/usr/bin/python3
""" class Student that defines a student by
Public instance attributes """

class Student:
    """ class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Initialize a new Student with specified attributes
        Args:
        first_name (string): student first name
        last_name (string): student last name
        age (int): student age

    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        Args:
            attrs (list): where attributes will be retrieved

        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved
        Otherwise, all attributes must be retrieved
        """
        
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance
        Args:
        json (dictionary): what will be used to replace the attributes with
        """

        for k, v in json.items():
            setattr(self, k, v)
