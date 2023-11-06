#!/usr/bin/python3
"""
MyInt class.
"""


class MyInt(int):
    """int"""
    def __new__(cls, *args, **kwargs):
        """new"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """eq"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ne"""
        return super().__eq__(other)
