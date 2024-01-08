#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        first = tuple_a[0] + tuple_b[0]
        second = tuple_a[1] + tuple_b[1]
        t = first, second
        return t
