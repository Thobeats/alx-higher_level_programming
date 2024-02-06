#!/usr/bin/python3
"""creates a Rectangle class that inherits the BaseGeometry class"""


class Rectangle(BaseGeometry):
    """rectangle inherits from geometry"""

    def __init__(self, width, height):
        self.integer_validate("width", width)
        self.__width = width
        self.integr_validate("height", height)
        self.__height = height
