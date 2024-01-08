#!/usr/bin/python3
"""  Subclass Square that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ class Square"""

    def __init__(self, size):
        """ Instantiation with size: def __init__(self, size
        to initialize square
        Args:
            size: square size in int
        """

        
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Area of the square """
        return self.__size * self.__size

    def __str__(self):
        """ print() will print, and str() will return
        the square description: [Square] <width>/<height>
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


