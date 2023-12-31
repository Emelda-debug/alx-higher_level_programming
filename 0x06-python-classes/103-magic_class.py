#!/usr/bin/python3

"""Python class MagicClass that does exactly the same as given  Python bytecode."""

import math

class MagicClass:
    """ Represents circle."""

    def __init__(self, radius = 0):
        """ Initialization.

        Args:
            radius(int/float): Radius of MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return MagicClass area."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return MagicClass circumference."""
        return ( 2 * math.pi * self.__radius)

