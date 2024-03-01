#!/usr/bin/python3
""" a class that defines a Student """


class Student():
    """ class to define student """

    def __init__(self, first_name, last_name, age):
        """ initialize the student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return a dictionary rep of the class """
        if isinstance(attrs, list):
            newDict = {}
            for i in self.__dict__:
                for j in attrs:
                    if i == j:
                        newDict[i] = self.__dict__[i]
            return newDict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            if i == "first_name":
                self.first_name = json[i]
            if i == "last_name":
                self.last_name = json[i]
            if i == "age":
                self.age = json[i]
