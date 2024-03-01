#!/usr/bin/python3
""" write a function that writes text into a file in UTF8 """


def write_file(filename="", text=""):
    """ writes the text into the file """

    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
