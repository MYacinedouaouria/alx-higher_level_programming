#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 0):
        t1_a = 0
        t2_a = 0
    elif (len(tuple_a) == 1):
        t1_a = tuple_a[0]
        t2_a = 0
    else:
        t1_a = tuple_a[0]
        t2_a = tuple_a[1]
    if (len(tuple_b) == 0):
        t1_b = 0
        t2_b = 0
    elif (len(tuple_b) == 1):
        t1_b = tuple_b[0]
        t2_b = 0
    else:
        t1_b = tuple_b[0]
        t2_b = tuple_b[1]
    new = (t1_a + t1_b, t2_a + t2_b)
    return new
