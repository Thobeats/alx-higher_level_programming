#!/usr/bin/python3
"""
This module contains a function that
finds the peak value in a list of
unsorted integers.
A peak value is a value that is
greater than its closest neighbours.
"""


def find_peak(list_of_integers):
    """
    Finds the peak value in the
    list of integers (unsorted)
    """
    if len(list_of_integers) == 0:
        return None

    for i, value in enumerate(list_of_integers):
        if (i > 0 and value > list_of_integers[i - 1]
                and value > list_of_integers[i + 1]):
            return value

    return list_of_integers[i]
