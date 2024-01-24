#!/usr/bin/python3
"""This Defines a Sqaure class"""


class Square:
    """
    A class representing a square.

    Attributes:
    - __size (int): The size of each side of the square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Parameters:
        - size (int): The size of each side of the square.
        """
        self.__size = size