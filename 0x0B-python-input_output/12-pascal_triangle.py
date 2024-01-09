#!/usr/bin/python3
""" returns a list of lists of integers representing the Pascal’s triangle of n """

def pascal_triangle(n):
    """ function for Pascal’s triangle of n
    Returns:
    list of lists of integers representing Pascal’s triangle of n
    """
    if n <= 0:
        return []

    t = [[1]]
    while len(t) != n:
        tri = t[-1]
        temp = [1]
        for x in range(len(tri) - 1):
            temp.append(tri[x] + tri[x + 1])

        temp.append(1)
        t.append(temp)
        return t
