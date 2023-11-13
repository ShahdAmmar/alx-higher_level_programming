#!/usr/bin/python3
""" Rectangle class module """
from models.base import Base


class Rectangle(Base):
    """ defining rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Intialization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """ width getter """
            return self.__width

        @width.setter
        def width(self, value):
            """ width setter """
            self.validate_number("width", value, False)
            self.__width = value

        @property
        def height(self):
            """ height getter """
            return self.__height

        @height.setter
        def height(self, value):
            """ height setter """
            self.validate_number("height", value, False)
            self.__height = value

        @property
        def x(self):
            """ x getter """
            return self.__x

        @x.setter
        def x(self, value):
            """ x setter """
            self.validate_number("x", value)
            self.__x = value

        @property
        def y(self):
            """ y getter """
            return self.__y

        @y.setter
        def y(self, value):
            """ y setter """
            self.validate_number("y", value)
            self.__y = value

        def validate_number(self, attrb, value, xy=True):
            """ checks if value is valid or not """
            if type(value) != int:
                raise TypeError("{} must be an integer".format(attrb))
            elif xy and value < 0:
                raise ValueError("{} must be >= 0".format(attrb))
            elif not xy and value <= 0:
                raise ValueError("{} must be > 0".format(attrb))
