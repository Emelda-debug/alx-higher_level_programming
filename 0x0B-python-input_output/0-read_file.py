#!/usr/bin/python3
"""  function that reads a text file (UTF8) and prints it to stdout """
def read_file(filename=""):
    """ will read  a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
