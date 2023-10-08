#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for line in matrix:
        for i, j in enumerate(line):
            if i == len(line) - 1:
                print("{:d}".format(j))
            else:
                print("{:d} ".format(j), end="")
