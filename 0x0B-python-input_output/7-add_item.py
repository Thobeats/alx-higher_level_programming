#!/usr/bin/python3
""" add all Python arguments to a list and save to file """

from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    argumentList = load_from_json_file("add_item.json")
except FileNotFoundError:
    argumentList = []

argumentList += argv[1:]
save_to_json_file(argumentList, "add_item.json")
