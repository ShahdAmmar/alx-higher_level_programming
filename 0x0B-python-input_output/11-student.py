#!/usr/bin/python3
""" defining Student Class """


class Student:
    """ represents student """
    def __init__(self, first_name, last_name, age):
        """ initialize instances """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns dictionary representation of a instances """
        try:
            for atr in attrs:
                if type(atr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dictt = dict()
        for k, val in self.__dict__.items():
            if k in attrs:
                dictt[k] = val
        return dictt

    def reload_from_json(self, json):
        """ replaces attributes of Student instance """
        for k, val in json.items():
            if k in self.__dict__:
                self.__dict__[k] = val
