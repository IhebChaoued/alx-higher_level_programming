#!/usr/bin/python3
"""Square/Rec"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""
    def __init__(self, size):
        """class"""
        super().__init__(size, size)

    def __str__(self):
        """str"""
        return "[Square] {}/{}".format(self.__width, self.__height)
