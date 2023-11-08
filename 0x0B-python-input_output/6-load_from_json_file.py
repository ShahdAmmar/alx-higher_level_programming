#!/usr/bin/python3
""" defining load_from_json_file function """
import json


def load_from_json_file(filename):
    """ creates object from json string """
    with open(filename, 'r', encoding='utf-8') as fl:
        objectt = json.load(fl)
        return objectt
