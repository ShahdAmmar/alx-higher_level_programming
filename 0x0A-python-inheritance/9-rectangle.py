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

    def area(self):
        """ calculates area """
        return self.__width * self.__height

    def __str__(self):
        """ string representation """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
