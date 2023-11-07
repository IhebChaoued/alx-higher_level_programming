#!/usr/bin/python3
"""object to text file"""


import json


def save_to_json_file(my_obj, filename):
    """obj json"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
