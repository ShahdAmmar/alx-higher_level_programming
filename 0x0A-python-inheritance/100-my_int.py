#!/usr/bin/python3
""" MyInt class Module """


class MyInt(int):
    """ rebel verion of integers """
    def __new__(cls, *args, **kwargs):
        """ cretaes new instance of class """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eql__(self, othr):
        """ == is != """
        return int(self) != othr

    def __neq__(self, othr):
        """ != is == """
        return int(self) == othr
