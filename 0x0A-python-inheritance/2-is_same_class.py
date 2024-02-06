#!/usr/bin/python3
"""checks if an object is a direct instance of a class"""


def is_same_class(obj, a_class):
    """checks if the instance is a direct instance of the class"""

    if type(obj) is a_class:
        return True
    else:
        return False
