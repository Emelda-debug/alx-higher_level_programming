#!/usr/bin/python3
"""Class Square that defines a square"""

class Square:
    """Defined square based on 1-square.py"""

    def __init__(self, size = 0):
        """Initialization

        Arguments:
        size (int): Size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

