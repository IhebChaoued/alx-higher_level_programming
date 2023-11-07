#!/usr/bin/python3
"""stdin"""


import sys


def print_stats(file_size, status_counts):
    """stdin"""
    print("File size: {}".format(file_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))


def main():
    try:
        line_number = 0
        total_file_size = 0
        status_counts = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0,
        }

        for line in sys.stdin:
            line_number += 1
            parts = line.split()
            if len(parts) >= 7:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_file_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1

            if line_number % 10 == 0:
                print_stats(total_file_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_file_size, status_counts)
