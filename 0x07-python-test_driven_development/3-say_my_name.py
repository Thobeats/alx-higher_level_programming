#!/usr/bin/python3
""" Prints out the firstname and the lastname """


def say_my_name(first_name, last_name=""):
    """ checks for the firstname and the lastname """
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
