#!/usr/bin/python3
""" Creation of class Rectangle that inherits BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ class inherits BaseGeometry"""

    def __init__(self, width, height):
        """ method to insantiate the class
        Args:
        width (int): int rectangle width
        height (int): int rectangle height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height


