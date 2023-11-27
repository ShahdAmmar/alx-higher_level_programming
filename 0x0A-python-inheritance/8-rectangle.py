#!/usr/bin/python3
""" Rectangle class Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ subclass for rectangle """
    def __init__(self, width, height):
        """ Intialization """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
