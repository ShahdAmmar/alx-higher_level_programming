#!/usr/bin/python3
""" defining save_to_json_file fuction """
import json


def save_to_json_file(my_obj, filename):
    """ write object into text file """
    with open(filename, 'w', encoding='utf-8') as fl:
        json_text = json.dumps(my_obj)
        fl.write(json_text)
