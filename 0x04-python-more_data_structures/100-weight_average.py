#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    j = 0
    for tp in my_list:
        number += tp[0] * tp[1]
        j += tp[1]
    return(number/j)
