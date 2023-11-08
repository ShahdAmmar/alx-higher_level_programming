#!/usr/bin/python3
""" defining append_after function """


def append_after(filename="", search_string="", new_string=""):
    """ appends new_string into filename """
    with open(filename, 'r', encoding='utf-8') as fl:
        lines = list()
        line = fl.readline()
        while line != "":
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
            line = fl.readline()

    with open(filename, 'w', encoding='utf-8') as fl:
        fl.writelines(lines)
