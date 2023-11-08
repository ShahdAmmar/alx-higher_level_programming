#!/usr/bin/python3
""" Task 7 Script """

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])
try:
    old = load_from_json_file('add_item.json')
except Exception:
    old = []
old.extend(args)
save_to_json_file(old, 'add_item.json')
