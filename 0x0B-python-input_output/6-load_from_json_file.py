#!/usr/bin/python3
""" write a function that creates object from a JSON file """


def load_from_json_file(filename):
    """ load from a json file """
    import json

    with open(filename, "r", encoding="utf-8") as fl:
        return json.load(fl)
