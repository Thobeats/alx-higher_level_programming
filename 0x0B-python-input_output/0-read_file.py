#!/usr/bin/python3
""" create a function that reads a file and prints it to stdout """


def read_file(filename=""):
    """ reads a file and prints to stdout """

    with open(filename, "r", encoding="utf-8") as fl:
        read_file = fl.read();
        print(read_file);
