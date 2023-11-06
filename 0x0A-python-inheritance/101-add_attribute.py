#!/usr/bin/python3
"""
add_attribute.
"""


def add_attribute(obj, attribute, value):
    """
    Add a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
