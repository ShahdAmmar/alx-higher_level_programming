#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_lst = set(my_list)
    result = 0
    for n in uniq_lst:
        result += n
    return result
