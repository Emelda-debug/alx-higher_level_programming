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

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Function to find the area pf the rectangle """
        return self.__width * self.__height

    def __str__ (self):
        """ return the [Rectangle] <width>/<height> """

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


