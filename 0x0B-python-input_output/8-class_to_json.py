#!/usr/bin/python3
""" returns the dictionary description of a class """


def class_to_json(obj):
    """ returns the dict description """
    return obj.__dict__
