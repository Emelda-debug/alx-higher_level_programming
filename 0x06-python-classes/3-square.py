#!/usr/bin/python3
"""class Square that defines a square."""

class Square:
    """Defined square based on 2-square.py."""

    def __init__(self, size = 0):
        """Initialization.

        Args:
        size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method: def area(self) that returns the current square area."""
        return (self.__size * self.__size)

