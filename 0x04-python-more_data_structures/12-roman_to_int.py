#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    integer = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
    roman_numerals = 0
    for x in range(len(roman_string)):
        if x > 0 and integer[roman_string[x]] > integer[roman_string[x - 1]]:
            roman_numerals += integer[roman_string[x]] - 2 * \
                    integer[roman_string[x - 1]]
        else:
            roman_numerals += integer[roman_string[x]]
    return roman_numerals
