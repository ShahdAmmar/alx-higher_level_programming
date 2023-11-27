#!/usr/bin/python3
""" inherits_from Module """


def inherits_from(obj, a_class):
    """ determines if object is a subclass """
    return (type(obj) != a_class and isinstance(obj, a_class))
