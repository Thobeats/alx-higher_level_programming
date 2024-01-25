#!/usr/bin/python3
"""This Defines a Square class"""


class Square:
    """
    A class representing a square.

    Attributes:
    - __size (int): The size of each side of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

    def area(self):
        """
        Computes the square value of the Square Instance

        Returns:
        - int: The area of the square
        """
        return pow(self.__size, 2)

    @property
    def size(self):
        """
        Retrieves the size value

        Returns:
        - int: The size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size value

        Parameters:
        - value (int): The new size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position coordinates

        Returns:
        - tuple: The position coordinates
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position coordinates

        Parameters:
        - value (tuple): The new coordinates
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("Tuple must be a tuple of two positive integers")

        self.__position = value

    def my_print(self):
        """
        Prints the value of the square using #

        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
