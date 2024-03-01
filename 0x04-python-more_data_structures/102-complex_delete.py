#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        delKey = False
        for key, val in a_dictionary.items():
            if val == value:
                delKey = key
        if delKey:
            del a_dictionary[delKey]
            return (complex_delete(a_dictionary, value))
    return a_dictionary
