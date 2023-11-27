#!/usr/bin/python3
""" Module for lookup function """


def lookup(obj):
    """ looks up for attributes
    Args: obj
    Returns: list of attributes
    """
    return (dir(obj))
