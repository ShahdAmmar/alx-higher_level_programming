#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    summ = 0
    if argc != 0:
        for i in range(argc):
            summ += int(argv[i + 1])
    print(summ)
