#!/usr/bin/python3
"""checks if an obj is an instance of the sub class of a class"""


def inherits_from(obj, a_class):
    """checks if the obj is an instance of the sub class
    but not the direct instance of the class"""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False

