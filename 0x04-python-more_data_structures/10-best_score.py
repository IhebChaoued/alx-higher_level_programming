#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    highest_score = 0
    best_student = None

    for key, value in a_dictionary.items():
        if value > highest_score:
            highest_score = value
            best_student = key
    return best_student
