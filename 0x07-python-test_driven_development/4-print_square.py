#!/usr/bin/python3
""" prints a square with the character #"""
def print_square(size):
    """ prints a square with the character
    Args:
    size is the size length of the square

    Returns:
    printed square

    Raises:
    TypeError: size must be an integer
    TypeError: size must be an integer
    ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")



