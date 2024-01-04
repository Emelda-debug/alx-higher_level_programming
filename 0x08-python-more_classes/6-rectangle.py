#!/usr/bin/python3
""" empty class Rectangle that defines a rectangle """

class Rectangle:
    """ empty class Rectangle that defines a rectangle
    Attributes:
    number_of_instances: The number of Rectangle instances
    """
    number_of_instances = 0

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

        def __str__(self):
            """ Returns rectangle defined by # """
            if self.__width == 0 or self.__height == 0:
                return ("")

            rectangle = []
            for x in range(self.__height):
                [rectangle.append('#') for y in range(self.__width)]
                if x != self.__height - 1:
                    rectangle.append("\n")
                    return ("".join(rectangle))

        def __repr__(self):
            """ return a string representation of the rectangle to be able to recreate a new instance by using eval()"""
            rectangle = "Rectangle(" + str(self.__width)
            rectangle += ", " + str(self.__height) + ")"
            return (rectangle)

        def __del__(self):
            """ prints the message Bye rectangle... """
            type(self).number_of_instances -= 1
            print("Bye rectangle...")
