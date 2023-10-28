#!/usr/bin/python3
""" Square Class Module """


class Square:
    """ Defines a Square class """

    def __init__(self, size=0):
        """ Initilization:
        Attributes:
            size: length of square size
        """
        self.size = size

    @property
    def size(self):
        """ Property of length of square side
        Raises:
            TypeError: if not int
            ValueError: if < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ defines area method """
        sq_area = self.__size ** 2
        return sq_area

    def my_print(self):
        """ Print Square """
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='\n' if j == self.size - 1 and i != j else '')
        print()
