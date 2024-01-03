#!/usr/bin/python3

def remove_char_at(str, n):
    first = str[:n]
    second = str[n+1:]
    result = first + second
    return result
