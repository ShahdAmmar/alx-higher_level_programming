#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = 0
    max_key = None

    for k, v in a_dictionary.items():
        if v > max_score:
            max_score = v
            max_key = k
    return max_key
