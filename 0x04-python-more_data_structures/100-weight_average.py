#!/usr/bin/python3
def weight_average(my_list=[]):
    x, y = 0, 0
    if my_list == []:
        return 0
    for i, j in my_list:
        x += i * j
        y += j
    x /= y
    return x
