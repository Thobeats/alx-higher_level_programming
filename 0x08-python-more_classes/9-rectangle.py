#!/usr/bin/python3
""" A class that defines a rectangle """


class Rectangle:
    """
        A class representing a rectangle

        Attributes:
        - __width (int): The width property of the Rectangle
        - __height (int): The height property of the Rectangle
        - number_of_instances (int): the amount of instances existing
        - print_symbol (string): the symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        if type(value) not in [int]:
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
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
        - int: the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
        - int: the perimeter of the rectangle
        """
        if self.__width == 0 and self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Prints out the string representation of the Rectangle class
        """
        output = ""
        if (self.__width == 0 and self.__height == 0):
            return ""
        for i in range(self.__height):
            for i in range(self.__width):
                output += str(self.print_symbol)
            output += "\n"
        output = output[:-1]
        return (output)

    def __repr__(self):
        """
        Returns a formal string rep of the rectangle
        """
        rep__ = "Rectangle(%s, %s)" % (self.__width, self.__height)
        return (rep__)

    def __del__(self):
        """
        Prints a bye message on delete
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the bigger rectangle based on area
        """
        if not rect_1 or not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not rect_2 or not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
