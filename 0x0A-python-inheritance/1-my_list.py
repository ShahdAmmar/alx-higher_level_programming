#!/usr/bin/python3
""" Module for MyList class """


class MyList(list):
    """ defining MyList class """
    def print_sorted(self):
        """ prints the list """
        print(sorted(self))
