#!/usr/bin/python3
""" empty class Rectangle that defines a rectangle """

class Rectangle:
    """ empty class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ defines a new rectangle 
        Args:
        height: height of new rectangle (int)
        width: width of new rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ Get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ Get the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            """ Returns rectangle area """
            return (self.__width * self.__height)

        def perimeter(self):
            """ Returns rectangle perimeter """
            if self.__width == 0 or self.__height == 0:
                return (0)
            return ((self.__width * 2) + (self.__height * 2))

