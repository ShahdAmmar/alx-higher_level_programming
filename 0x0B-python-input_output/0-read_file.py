#!/usr/bin/python3
""" read_file function """


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as fl:
        read_data = fl.read()
        print(read_data, end="")
