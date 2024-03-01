#!/usr/bin/python3
""" a function to insert a line of text after a line contataining a specific string """

def append_after(filename="", search_string="", new_string=""):

    with open(filename,"a", encoding="utf-8") as fl:
        
