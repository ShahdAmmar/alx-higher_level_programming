#!/usr/bin/python3

for c in range(ord('Z'), ord('A') - 1, -1):
    if c % 2 == 0:
        c += 32
    print("{:c}".format(c), end="")
