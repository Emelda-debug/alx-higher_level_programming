#!/usr/bin/python3
""" Function that returns True if the object is exactly
an instance of a class that inherited from; otherwise False """

def is_kind_of_class(obj, a_class):
    """ To verify if an object is exactly an instance of the specified class
    Args:
        obj: object to check
        a_class: the specified class to be checked

    Returns:
        True: if the object is exactly an instance of the specified class
        Otherwise: false
        """

        if isinstance(obj, a_class):
            return True
         return False

