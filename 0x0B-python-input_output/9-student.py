#!/usr/bin/python3
""" defining Student Class """


class Student:
    """ represents student """
    def __init__(self, first_name, last_name, age):
        """ initialize instances """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns dictionary representation of a instances """
        return self.__dict__
