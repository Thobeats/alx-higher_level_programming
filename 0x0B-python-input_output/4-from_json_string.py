#!/usr/bin/python3
""" prints out Python Object from JSON """


def from_json_string(my_str):
    """ imports the json module and return the python object """
    import json

    return json.loads(my_str)
