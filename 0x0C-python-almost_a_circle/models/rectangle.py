#!/usr/bin/python3
""" define a class Rectangle that inherits from base """


from models.base import Base


class Rectangle(Base):
    """ initialize an instance of the rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        This is a width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value to the width property
        """
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0") """
        self.mustBeInt("width", value)
        self.mustBeGreaterThanZero("width", value)
        self.__width = value

    @property
    def height(self):
        """
        this is the height getter
        it gets the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is the height setter
        it sets the value to the height property
        """
        self.mustBeInt("height", value)
        self.mustBeGreaterThanZero("height", value)
        self.__height = value

    @property
    def x(self):
        """
        This is the getter for the x property
        it returns the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This is the setter function for the x property
        """
        self.mustBeInt("x", value)
        self.mustBeGreaterOrEqualZero("x", value)
        self.__x = value

    @property
    def y(self):
        """
        This is the getter for the y property
        It returns the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This is the setter for the y property
        It sets a new value for y
        """
        self.mustBeInt("y", value)
        self.mustBeGreaterOrEqualZero("y", value)
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        """
        prints out the rectangle with # character
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            print(" "*self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        reassign values to the rectangle properties
        """
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        elif kwargs and len(kwargs) > 0:
            for j in kwargs:
                if j == "id":
                    self.id = kwargs[j]
                if j == "width":
                    self.__width = kwargs[j]
                if j == "height":
                    self.__height = kwargs[j]
                if j == "x":
                    self.__x = kwargs[j]
                if j == "y":
                    self.__y = kwargs[j]

    def __str__(self):
        """
        print out a string rep of the rectangle class
        """
        str_rep = "[Rectangle] ({:d}) {}/{} - {}/{}"
        return (str_rep.format(
            self.id, self.__x, self.__y,
            self.__width, self.__height))

    def to_dictionary(self):
        """
            Returns the dictionary rep of the rectangle
        """
        rect_dictionary = {}
        rect_dictionary["id"] = self.id
        rect_dictionary["width"] = self.__width
        rect_dictionary["height"] = self.__height
        rect_dictionary["x"] = self.__x
        rect_dictionary["y"] = self.__y
        return rect_dictionary

    def mustBeInt(self, key, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(key))

    def mustBeGreaterThanZero(self, key, value):
        if value <= 0:
            raise ValueError("{} must be > 0".format(key))

    def mustBeGreaterOrEqualZero(self, key, value):
        if value < 0:
            raise ValueError("{} must be >= 0".format(key))
