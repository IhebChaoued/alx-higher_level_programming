#!/usr/bin/python3
"""check"""


class Square:
    """check"""
    def __init__(self, size=0):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    size = property(get_size, set_size)

    def area(self):
        return self.__size ** 2
