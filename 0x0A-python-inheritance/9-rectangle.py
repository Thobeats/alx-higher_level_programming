#!/usr/bin/python3
"""creates a Rectangle class that inherits the BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle inherits from geometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """string representation of Rectangle"""
        str_rep = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return str_rep
