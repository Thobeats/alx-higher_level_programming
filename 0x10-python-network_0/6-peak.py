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
    l, r = 0, len(list_of_integers) - 1
 
    while l <= r:
        mid = l + ((r - l) // 2)
        if (mid > 0 and list_of_integers[mid] <
            list_of_integers[mid - 1]):
            """ check on the left side"""
            r = mid - 1
        elif (mid < len(list_of_integers) - 1 and list_of_integers[mid] <
                list_of_integers[mid + 1]):
            """ check on the right side"""
            l = mid + 1
        else:
            return list_of_integers[mid]
    
