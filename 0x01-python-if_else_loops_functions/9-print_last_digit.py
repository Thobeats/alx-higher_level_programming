#!/usr/bin/python3
def print_last_digit(c):
    if c > 0:
        ld = c % 10
    else:
        ld = -(-c % 10)
    print(ld, end='')
    return (ld)
