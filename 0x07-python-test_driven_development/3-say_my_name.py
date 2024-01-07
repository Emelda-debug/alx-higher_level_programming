#!/usr/bin/python3
""" function that prints My name is <first name> <last name>"""

def say_my_name(first_name, last_name=""):
    """ prints names 
    Args:
    first_name- first name
    last_name- last name (string)

    Returns:
    first and last name

    Raises:
    TypeError: first_name must be a string or last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
