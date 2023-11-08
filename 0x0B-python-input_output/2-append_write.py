#!/usr/bin/python3
""" defining append_write function """


def append_write(filename="", text=""):
    """ appends text into filename """
    with open(filename, 'a', encoding='utf-8') as fl:
        return fl.write(text)
