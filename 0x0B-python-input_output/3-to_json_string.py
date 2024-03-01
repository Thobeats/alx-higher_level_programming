#!/usr/bin/python3
""" prints out the JSON rep of an object """


def to_json_string(my_obj):
    """ imports the json module and prints out the string rep
        of the object """
    import json

    return json.dumps(my_obj)
