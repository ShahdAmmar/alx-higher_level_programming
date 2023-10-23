#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    try:
        while cnt < x:
            print("{:d}".format(my_list[cnt]), end='')
            cnt += 1
    except (ValueError, TypeError):
        pass
    print()
    return cnt
