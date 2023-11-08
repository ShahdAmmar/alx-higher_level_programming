#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, 'r') as fl:
        read_data = fl.read()
        print(read_data)
