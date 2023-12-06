#!/usr/bin/python3
def no_c(my_string):
    str2 = ""
    for x in my_string:
        if (x != 'c') and (x != 'C'):
            str2 += x
    return (str2)
