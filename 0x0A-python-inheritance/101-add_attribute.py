#!/usr/bin/python
""" function that adds a new attribute to an object if it’s possible """

def add_attribute(objct, atrbt, vlue):
    """ Should add a new attribute to an object if it’s possible
    Args:
    objct: object to add the attribute to
    atrbt: the attribute to be added
    vlue: attribute value

    Raises:
    TypeError:
     if object can’t have new attribute: "can't add new attribute"
     """

     if not hasattr(obj, "__dict__"):
         raise TypeError("can't add new attribute")
     setattr(obj, att, value)
