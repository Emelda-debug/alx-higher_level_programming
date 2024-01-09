#!/usr/bin/python3
""" unction that inserts a line of text to a file, after each
line containing a specific string
"""
def append_after(filename="", search_string="", new_string=""):
    """ function inserts  a line of text to a file,
    Args:
    filename (string): file that will have ext inserted into
    search_string (string): the string that will be serached for
    new_string (string): the string that will be inserted
    """
    txt = ""
    with open(filename) as r:
        for ln in r:
            txt += ln
            if search_string in ln:
                txt += new_string

    with open(filename, "w") as w:
        w.write(text)
