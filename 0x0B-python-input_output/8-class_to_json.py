#!/usr/bin/python3
""" defining class_to_json function """


def class_to_json(obj):
    """ returns dictionary representation of an object """
    return obj.__dict__
