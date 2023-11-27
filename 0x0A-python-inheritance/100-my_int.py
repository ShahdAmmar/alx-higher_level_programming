#!/usr/bin/python3
""" MyInt class Module """


class MyInt(int):
    """ rebel verion of integers """
    def __nwclass__(cls, *args, **kargs):
        """ cretaes new instance of class """
        return super(MyInt, cls).__nwclass__(cls, *args, **kargs)

    def __eql__(self, other):
        """ == is != """
        return int(self) != other

    def __neql__(self, other):
        """ != is == """
        return int(self) == other
