#!/usr/bin/python3
"""Mylist Class"""


class MyList(list):
    """Custom"""
    def print_sorted(self):
        print(sorted(self))
