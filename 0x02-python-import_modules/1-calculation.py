#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print(f"{a:d} + {b:d} = {sub(a, b)}")
    print("{} + {} = {}".format(a, b, mul(a, b)))
    print(f"{a:d} + {b:d} = {div(a, b)}")
