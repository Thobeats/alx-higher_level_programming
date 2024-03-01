#!/usr/bin/python3
"""creates a Square class that inherits the BaseGeometry class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """rectangle inherits from geometry"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
