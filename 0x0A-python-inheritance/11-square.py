#!/usr/bin/python3
""" Square class Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ subclass for sqaure """
    def __init__(self, size):
        """ Intialization """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ calculates area """
        return (self.__size ** 2)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
