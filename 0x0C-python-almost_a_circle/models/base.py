#!/usr/bin/python3
""" define the class Base """


class Base:
    """ keeps the record of all instances """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes a new base instance with an id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the json rep of a dictionary
        """
        import json

        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
