#!/usr/bin/python3
"""checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """use the isinstance method to check"""

    if type(obj) is a_class:
        return True
    else:
        return False

