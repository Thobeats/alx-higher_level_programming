#!/usr/bin/python3
"""class MyList inherits list class"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
