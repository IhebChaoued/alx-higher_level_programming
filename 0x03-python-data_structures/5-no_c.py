#!/usr/bin/python3
def no_c(my_string):
    cant_c = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            cant_c += char
        return cant_c
