#!/usr/bin/python3
""" write a function that writes an object into a file using JSON """


def save_to_json_file(my_obj, filename):
    """ wite an object into a file """
    import json

    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(json.dumps(my_obj))
