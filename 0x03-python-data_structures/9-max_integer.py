#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    first_char = my_list[0]
    for i in my_list:
        if i > first_char:
            first_char = i
    return first_char
