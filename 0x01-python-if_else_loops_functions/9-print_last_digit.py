#!/usr/bin/python3
def islower(c):
    if c > 0:
        ld = c % 10
    else:
        ld = -(-c % 10)

    print(ld)
