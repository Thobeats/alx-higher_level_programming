#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = 1

    while idx <= len(my_list):
        print("{:d}".format(my_list[len(my_list) - idx]))
        idx = idx + 1
