#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n > len(str):
        print("Invalid Offset")
        return 0
    first = str[:n]
    second = str[n+1:]
    result = first + second
    return result
