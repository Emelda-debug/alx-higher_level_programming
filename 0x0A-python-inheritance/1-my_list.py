#!/usr/bin/python3
""" Creation of class MyList that inherits from list"""

class MyList():
   
    """ MyList class that will be used for inheritance"""
    
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort)"""
        print(sorted(self))
