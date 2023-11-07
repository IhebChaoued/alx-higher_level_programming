#!/usr/bin/python3
"""Read File"""


def read_file(filename=""):
    """
    Read the contents of a text file and print it.
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")
