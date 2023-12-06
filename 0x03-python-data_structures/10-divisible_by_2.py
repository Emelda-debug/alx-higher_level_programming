#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean_list = my_list[:]
    for cnt, x in enumerate(my_list):
        if x % 2 == 0:
            boolean_list[cnt] = True
        else:
            boolean_list[cnt] = False
    return (boolean_list)
