#!/usr/bin/python3
"""Find a peak in an unsorted list of integers."""

def find_peak(lst):
    """Finds a peak in an unsorted list."""
    if not lst:
        return None

    low, high = 0, len(lst) - 1

    while low < high:
        mid = (low + high) // 2

        if lst[mid] > lst[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return lst[low]
