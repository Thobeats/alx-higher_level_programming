#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary)
    keys.sort()
    for i in keys:
        print(f"{i} : {a_dictionary[i]}")
