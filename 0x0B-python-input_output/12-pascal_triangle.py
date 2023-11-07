#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """Pascal"""
    if n <= 0:
        return []

    def generate_next_row(previous_row):
        if not previous_row:
            return [1]
        next_row = [1]
        for i in range(1, len(previous_row)):
            next_row.append(previous_row[i - 1] + previous_row[i])
        next_row.append(1)
        return next_row

    triangle = []
    row = []
    for _ in range(n):
        row = generate_next_row(row)
        triangle.append(row)

    return triangle
