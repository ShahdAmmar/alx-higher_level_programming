#!/usr/bin/python3
""" defining to_json_string function """
import json


def to_json_string(my_obj):
    """ returns json respresentation """
    json_string = json.dumps(my_obj)
    return json_string
