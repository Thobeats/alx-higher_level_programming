#!/usr/bin/python3
"""class Mylist inherits list class"""


class Mylist(list):
    """class that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
