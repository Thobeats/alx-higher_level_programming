#!/usr/bin/pyhton3

def remove_char_at(str, n):

    if n < 0 or n > len(str):
        print("Invalid offset")
        return 0
    first_part = str[:n]
    second_part = str[n+1:]
    result = first_part + second_part
    return result
