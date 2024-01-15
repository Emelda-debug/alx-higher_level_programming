#!/usr/bin/python3
""" Rectangle class """
class Rectangle(Base):
    """ class to represent a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Private instance attributes, each with its own public getter and setter:
        Args:
        width: width
        height: height
        x:x coordinate of the new Rectangle
        y: y coordinate of the new Rectangle
        Raises:
        TypeError: <name of the attribute> must be an integer
        TypeError: x and y must be an int
        ValueError: <name of the attribute> must be >= 0
        ValueError: <name of the attribute> must be > 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

@property
def width(self):
    """ Get rectangle width """
    return self.__width

@width.setter
def width(self, value):
    if type(value) != int:
        raise TypeError("width must be an integer")
    if value <= 0:
        raise ValueError("width must be > 0")
    self.__width = value

@property
def height(self):
        """ Get rectangle height"""
        return self.__height

@height.setter
def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

@property
def x(self):
    """ get the x coordinate """
    return self.__x

@x.setter
def x(self, value):
    if type(value) != int:
        raise TypeError("x must be an integer")
    if value < 0:
        raise ValueError("x must be >= 0")
    self.__x = value

@property
def y(self):
    """ get the y coordinate """
    return self.__y
@y.setter
def y(self, value):
    if type(value) != int:
        raise TypeError("y must be an integer")
    if value < 0:
        raise ValueError("y must be >= 0")
    self.__y = value

def area(self):
    """ Return rectangle area """
    return self.width * self.height

def display(self):
    """ print rectangle using # """
    if self.width == 0 or self.height == 0:
        print("")
        return
    [print("") for y in range(self.y)]
    for i in range(self.height):
        [print(" ", end="") for x in range(self.x)]
        [print("#", end="") for w in range(self.width)]
        print("")

def update(self, *args, **kwargs):
    """ update class rectangle by adding the public method  
    Args:
    *args is the list of arguments - no-keyworded arguments
    1st argument should be the id attribute
    2nd argument should be the size attribute
    3rd argument should be the x attribute
    4th argument should be the y attribute
    **kwargs can be thought of as a double pointer to a dictionary
    """
    if args and len(args) != 0:
        j = 0
        for arg in args:
            if j == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
                    elif j == 1:
                        self.width = arg
                        elif j == 2:
                            self.height = arg
                            elif j == 3:
                                self.x = arg
                                elif j == 4:
                                    self.y = arg
                                    j += 1

elif kwargs and len(kwargs) != 0:
    for l, b in kwargs.items():
        if l == "id":
            if b is none:
                self.__init__(self.width, self.height, self.x, self.y)
            else:
                self.id = b
            elif l == "width":
                self.width = b
            elif l == "height":
                self.height = b
            elif l == "x":
                self.x = b
            elif l == "y":
                self.y = b

def to_dictionary(self):
    """ public method that returns the dictionary representation of a Rectangle:"""
    return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }

def __str__(self):
    """ Return the print() and str() representation of the Rectangle """
    return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
            self.x, self.y,
            self.width, self.height)






    


      

