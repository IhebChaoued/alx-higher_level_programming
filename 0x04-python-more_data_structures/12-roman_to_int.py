#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_dictionary = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }

    total_values = [roman_dictionary[x] for x in roman_string]
    value = 0
    for i in range(len(total_values)):
        value += total_values[i]
        if i > 0 and total_values[i - 1] < total_values[i]:
            value -= total_values[i - 1] * 2
    return value
