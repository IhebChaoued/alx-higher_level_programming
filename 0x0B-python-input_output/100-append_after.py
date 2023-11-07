#!/usr/bin/python3
"""insert a line"""


def append_after(filename="", search_string="", new_string=""):
    """insertion"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
