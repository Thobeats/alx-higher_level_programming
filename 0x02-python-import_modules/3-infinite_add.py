#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    res = 0
    for i, j in enumerate(argv):
        if i == 0:
            continue
        res += int(j)
    print(f"{res:d}")
