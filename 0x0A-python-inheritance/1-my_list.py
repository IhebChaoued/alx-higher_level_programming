#!/usr/bin/python3
"""Mylist Class"""


class MyList(list):
    """Custom"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
