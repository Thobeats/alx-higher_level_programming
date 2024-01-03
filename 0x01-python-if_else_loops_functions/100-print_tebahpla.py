#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 > 0:
        alpha = chr(i).upper()
    else:
        alpha = chr(i)
    print("{}".format(alpha), end='')
