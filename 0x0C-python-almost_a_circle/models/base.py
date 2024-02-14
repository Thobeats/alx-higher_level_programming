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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves the json rep of the list objects of the
        class into a file
        """
        if list_objs is None:
            return "[]"

        list_dicts = []
        for instance in list_objs:
            list_dicts.append(instance.to_dictionary())
        filename = cls.__name__ + ".json"
        jsonListRep = cls.to_json_string(list_dicts)
        with open(filename, "w") as fout:
            return fout.write(jsonListRep)
