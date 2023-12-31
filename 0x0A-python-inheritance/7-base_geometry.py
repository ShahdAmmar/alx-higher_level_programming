#!/usr/bin/python3
""" BaseGeometry class Module """


class BaseGeometry:
    """ defining empty class """
    def area(self):
        """ calculates area """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validating values """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
