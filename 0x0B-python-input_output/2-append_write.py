#!/usr/bin/python3
""" function that appends a string to a text file
(UTF8) and returns the number of characters added"""

def append_ write(filename="", text=""):
    """ appends a string to a text file (UTF8) and
    returns the number of characters written
    Args:
    filename (str): name of file where string will be appended
    text (str): the text that will be written
    Returns:
    the number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

