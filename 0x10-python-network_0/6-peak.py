#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers
"""
def find_peak(list_of_integers):
    """ for this, I will be using brute force"""
    max_x = None
    for element in list_of_integers:
        if max_x is None or max_x < element:
            max_x = element
    return max_x

