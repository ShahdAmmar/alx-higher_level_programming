#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    lst = dir(hidden_4)
    for f in lst:
        if f[:2] != "__":
            print(f)
