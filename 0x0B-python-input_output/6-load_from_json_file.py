#!/usr/bin/python3
"""create object from json file"""


import json


def load_from_json_file(filename):
    """load"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
