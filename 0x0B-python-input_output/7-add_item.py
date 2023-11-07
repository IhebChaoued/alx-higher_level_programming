#!/usr/bin/python3
"""add all arguments"""


import sys

from 6-load_from_json_file import load_from_json_file
from 5-save_to_json_file import save_to_json_file


def main():
    """saving"""
    filename = "add_item.json"
    my_list = []

    if os.path.isfile(filename):
        my_list = load_from_json_file(filename)

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, filename)
