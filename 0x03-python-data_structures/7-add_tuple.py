#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[0] if len(tuple_a) > 0 else 0
    b = tuple_a[0] if len(tuple_a) > 1 else 0
    c = tuple_a[0] if len(tuple_a) > 0 else 0
    d = tuple_a[0] if len(tuple_a) > 1 else 0

    return (a + c, b + d)
