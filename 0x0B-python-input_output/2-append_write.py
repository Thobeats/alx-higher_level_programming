#!/usr/bin/python3
""" write a function that appends string at the end of a file """


def append_write(filename="", text=""):
    """ appends string to the end of the file """

    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
