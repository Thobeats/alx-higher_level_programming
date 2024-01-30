#!/usr/bin/python3
""" A class that defines a rectangle """


class Rectangle:
    """
        A class representing a rectangle

        Attributes:
        - __width (int): The width property of the Rectangle
        - __height (int): The height property of the Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the given width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    """ defines an a getter to get the private property width """
    @property
    def width(self):
        """
        Retrieves the value of the width property

        Returns:
        - int: the width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width

        Paramater:
        - value (int): The new width of the rectangle
        """
        if type(value) not in [int, float]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of the height property

        Returns:
        - int: the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the height

        Paramater:
        - value (int): The new height of the rectangle
        """
        if type(value) not in [int, float]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
