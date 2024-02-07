#!/usr/bin/python3
""" a class that defines a Student """


class Student:
    first_name
    last_name
    age

    def __init__(self, first_name, last_name, age):
        """ initialize the student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return a dictionary rep of the class """
        return self.__dict__
