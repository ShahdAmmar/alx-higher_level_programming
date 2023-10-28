#!/usr/bin/python3
""" Square Class Module """


class Square:
    """ Defines a Square class """

    def __init__(self, size=0):
        """ Initilization:
        Attributes:
            size: length of square side
        Raises:
            TypeError: if not int
            ValueError: if < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
