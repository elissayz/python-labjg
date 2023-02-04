#!/usr/bin/python3


def evens(n):
    arr = range(n+1)
    arr = filter(lambda x: (x % 2 == 0), arr)
    return list(arr)
