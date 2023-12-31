#!/usr/bin/python3
"""Class Square that defines a square."""

class Square:
    """Defined square based on 3-square.py."""

    def __init__(self, size = 0):
        """Initialization.

        Args:
        size (int): Size of the new square.
        """
        self.__size = size

        @property
        def size(self):
            """Get square current size."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """Public instance method: def area(self): that returns the current square area."""
        return (self.__size * self.__size)

