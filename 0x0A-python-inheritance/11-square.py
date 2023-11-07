#!/usr/bin/python3
"""
Square/Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """init"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area"""
        return super().area()

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
