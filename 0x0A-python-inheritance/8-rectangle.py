#!/usr/bin/python3
""" Creation of class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ class inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ method to insantiate the class
        Args:
        width: int rectangle width
        height: int rectangle height
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height


