#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = (-number % 10)
    elif number >= 0:
        num = number % 10
    print("{:d}".format(num), end="")
    return num
