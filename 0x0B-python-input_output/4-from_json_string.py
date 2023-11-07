#!/usr/bin/python3
"""return object by json string"""


import json


def from_json_string(my_str):
    """json str"""
    return json.loads(my_str)
