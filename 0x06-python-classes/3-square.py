#!/usr/bin/python3
"""This Defines a Square class"""


class Square:
    """
    A class representing a square.

    Attributes:
    - __size (int): The size of each side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Parameters:
        - size (int): The size of each side of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the square value of the Square Instance

        Returns:
        - int: The area of the square
        """
        return pow(self.__size, 2)
