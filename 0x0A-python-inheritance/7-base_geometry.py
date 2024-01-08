#!/usr/bin/python3
""" Creation of  empty class BaseGeometry """

class BaseGeometry:
    """ empty class created """

    def area(self):
        """ Public instance method that raises an Exception
        with the message area() is not implemented """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ public instance method that validates value
        Args:
        name: string that is the parameter name
        value: int value to validate

        Return: TypeError and Value error
        TypeErrors:
        if value is not an integer: <name> must be an integer
        if value =< 0: <name> must be greater than 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))



