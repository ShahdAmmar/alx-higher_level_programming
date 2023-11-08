#!/usr/bin/python3
""" defining pascal_triangle function """

def pascal_triangle(n):
    """ represent pascal's triangles """
    if n <= 0:
        return []

    trians = [[1]]
    while len(trians) != n:
        trian = trians[-1]
        temp = [1]
        for i in range(len(trian) - 1):
            temp.append(trian[i] + trian[i + 1])
        temp.append(1)
        trians.append(temp)
    return trian
