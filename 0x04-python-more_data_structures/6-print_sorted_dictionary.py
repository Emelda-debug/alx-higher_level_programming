#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_to_be_sorted = list(a_dictionary.keys())
    list_to_be_sorted.sort()
    for x in list_to_be_sorted:
        print("{}: {}".format (x, a_dictionary.get(x)))

