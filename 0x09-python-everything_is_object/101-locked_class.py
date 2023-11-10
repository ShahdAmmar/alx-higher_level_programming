#!/usr/bin/python3
""" defines LockedClass """


class LockedClass:
    """
    prevents intiating new LockedClass attributes unless 'first_name'
    """
    __slots__ = ["first_name"]
