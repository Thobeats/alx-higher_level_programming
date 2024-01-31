#!/usr/bin/python3
""" a function that idents a given text """


def text_indentation(text):
    """ checks for text """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    newLine = ""
    for char in text:
        # leading whitespace
        if char is " " and char is text[0] and newLine is "":
            newLine = "\n"
            continue
        # whitespaces after newline
        if char is " " and newLine is "\n":
            continue
        # matching character, print char, print newlines
        if char is "." or char is "?" or char is ":":
            print(char)
            print()
            newLine = "\n"
        else:
            print(char, end="")
            newLine = char
