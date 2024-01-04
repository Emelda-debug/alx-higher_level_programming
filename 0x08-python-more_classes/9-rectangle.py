#!/usr/bin/python3
""" empty class Rectangle that defines a rectangle """

class Rectangle:
    """ empty class Rectangle that defines a rectangle
    Attributes:
    number_of_instances: number of Rectangle instances
    print_symbol: symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

    """ initializes a new rectangle 
    Args:
    height: height of new rectangle (int)
    width: width of new rectangle

    Attributes:
    number_of_instances: The number of Rectangle instances.
    """

    type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle based on the area
        Args:
        rect_1: Retangle 1
        rect_2: Rectangle 2

        Raises:
        TypeError: If either of rect_1 or rect_2 is not a Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size
        Args:
        size: The width and height of the new Rectangle
        """
        return (cls(size, size))

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
