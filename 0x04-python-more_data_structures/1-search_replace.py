#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    list2 = my_list[:]
    for index, x in enumerate(list2):
        if x == search:
            list2[index] = replace
    return list2
