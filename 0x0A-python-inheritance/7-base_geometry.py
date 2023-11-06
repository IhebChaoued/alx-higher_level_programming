#!/usr/bin/python3
"""
BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry
    """
    def area(self):
        """compute"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
