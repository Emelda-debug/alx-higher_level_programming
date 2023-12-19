#!/usr/bin/python3
"""Class Square that defines a square."""

class Square:
    """Defined square based on 3-square.py."""

    def __init__(self, size = 0, position = (0,0)):
        """Initialization.

        Arguments:
        size (int): Size of the new square.
        positition (int, int): position of new square.
        """
        self.size = size
        self.position = position

        @property
        def size(self):
            """Get square current size."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        @property
        def position(self):
            """Get square current position."""
            return(self.__position)

     @position.setter
     def position(self,value):
         if (not isinstance(value, tuple) or
             len(value) != 2 or
             not all(isinstance(number, int) for number in value) or 
             not all(number >= 0 for number in value)):
         raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method: def area(self): that returns the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0
        print ("")
        return

    [print("") for x in range(0, self.__position[1])]
    for x in range(0, self.__size):
        [print("", end="") for y in range(self.__position[0])]
        [print("#", end="") for z in range(self.__size)]
            print("")
