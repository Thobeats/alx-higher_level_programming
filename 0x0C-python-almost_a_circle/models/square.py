#!/usr/bin/python3
""" define a Square class that inherits the Rectangle class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    define the Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        this is the size getter
        it gets the size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        This is the size setter
        it sets the value to the size property
        """
        self.mustBeInt("width", value)
        self.mustBeGreaterThanZero("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """
        print out a string rep of the square class
        """
        str_rep = "[Square] ({:d}) {}/{} - {}"
        return (str_rep.format(
            self.id, self.x, self.y,
            self.width))

    def update(self, *args, **kwargs):
        """
        reassign values to the square properties
        """
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        elif kwargs and len(kwargs) > 0:
            for j in kwargs:
                if j == "id":
                    self.id = kwargs[j]
                if j == "size":
                    self.size = kwargs[j]
                if j == "x":
                    self.x = kwargs[j]
                if j == "y":
                    self.y = kwargs[j]

    def to_dictionary(self):
        """
            Returns the dictionary rep of the square
        """
        rect_dictionary = {}
        rect_dictionary["id"] = self.id
        rect_dictionary["size"] = self.size
        rect_dictionary["x"] = self.x
        rect_dictionary["y"] = self.y
        return rect_dictionary
