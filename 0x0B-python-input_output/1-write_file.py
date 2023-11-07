#!/usr/bin/python3
"""Write string to a text file"""


def write_file(filename="", text=""):
    """String writing"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
