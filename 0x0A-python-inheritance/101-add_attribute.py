#!/usr/bin/python3
""" add_attributes function module """


def add_attribute(obj, attr, val):
    """ adds new attribute to an object if possible
    Args: obj, attr, val
    Raises: TypeError
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
