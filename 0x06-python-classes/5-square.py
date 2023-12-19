#!/usr/bin/python3
"""class Square that defines a square"""

class Square:
    """Defined square based on 3-square.py"""

    def __init__(self, size = 0):
        """Initialization

        Arguments:
        size (int) size of the new square
        """
        self.__size = size

        @property
        def size(self):
            """Get square current size"""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """Public instance method: def area(self): that returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        for x in range(0, self.__size):
            [print("#", end="") for y in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

