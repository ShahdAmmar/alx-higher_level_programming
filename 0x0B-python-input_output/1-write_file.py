#!/usr/bin/python3
""" defining write_file """


def write_file(filename="", text=""):
    """ write text into filename """
    with open(filename, 'w', encoding='utf-8') as fl:
        return fl.write(text)
