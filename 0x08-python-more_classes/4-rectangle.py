#!/usr/bin/python3
""" Defining empty class Rectangle"""


class Rectangle:
    """ Defining Rectangle class """
    def __init__(self, width=0, height=0):
        """ Intialize Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for private instant attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for private instant attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for private instant attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for private instant attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ calculate rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """ returns string """
        str_ = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                str_ += ("#" * self.__width)
                str_ += "\n" if i != self.__height - 1 else ""
        return str_

    def __repr__(self):
        """ returns string representation """
        return f"Rectangle({self.__width:d}, {self.__height:d})"
