#!/usr/bin/python3
""" class MyInt that inherits int """

class MyInt(int):
    """ will invert == and != because MyInt is a rebel lol"""

    def __eq__(self, value):
        """ method that uses == operator to compare the instances of the class """
        return self.real != value

    def __ne__(self, value):
        """ method to compare two objects using != """

        return self.real == value


