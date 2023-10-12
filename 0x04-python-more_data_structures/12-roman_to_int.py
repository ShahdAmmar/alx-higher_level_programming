#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    num = 0
    total_num = 0
    digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for c in reversed(roman_string):
        num = digits[c]
        total_num += num if total_num < num * 5 else -num
    return total_num
