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
        filename = cls.__name__ + ".json"
        list_dicts = []

        if list_objs is not None:
            for instance in list_objs:
                list_dicts.append(instance.to_dictionary())
            jsonListRep = cls.to_json_string(list_dicts)
        else:
            jsonListRep = "[]"
        with open(filename, "w") as fout:
            return fout.write(jsonListRep)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list represented by the string
        """

        if json_string is None:
            return list()
        import json
        loadedJson = json.loads(json_string)
        return loadedJson
    
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        using update method"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1, 0, 0)
        if cls.__name__ == "Square":
            instance = cls(1, 0, 0)
        instance.update(**dictionary)
        return instance
