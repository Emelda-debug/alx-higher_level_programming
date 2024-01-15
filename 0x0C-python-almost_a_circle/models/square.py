#!/usr/bin/python3
"""Creation of a square class  that inherits from square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor to initialize a new Square
        Args:
        size: size of new square
        x: x coordinate
        y: y coordinate
        id: id of new square
        """

        super().__init__(size, size, x, y, id)

        @property
        def size(self):
            """Get size of the Square."""
            return self.width

        @size.setter
        def size(self, value):
            self.width = value
            self.height = value

        def update(self, *args, **kwargs):
            """ update square
            Args:
            *args: : New attribute values
            - 1st argument represents id attribute
            - 2nd argument represents size attribute
            - 3rd argument represents x attribute
            - 4th argument represents y attribute
            *kwargs: New key pairs of attributes
            """
            if args and len(args) != 0:
                z = 0
                for arg in args:
                    if z == 0:
                        if arg is None:
                            self.__init__(self.size, self.x, self.y)
                        else:
                            self.id = arg
                        elif z == 1:
                            self.size = arg
                        elif z == 2:
                            self.x = arg
                        elif z == 3:
                            self.y = arg
                            z += 1

            elif kwargs and len(kwargs) != 0:
                for l, b in kwargs.items():
                    if l == "id":
                        if b is None:
                            self.__init__(self.size, self.x, self.y)
                        else:
                            self.id = b
                        elif l == "size":
                            self.size = b

        def to_dictionary(self):
            """ Return the dictionary representation of the Square """
            return {
                    "id": self.id,
                    "size": self.width,
                    "x": self.x
                    "y": self.y

                    }

        def __str__(self):
            """ "Return the print() and str() representation of a Square."""
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                    self.width)


