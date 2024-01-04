#!/usr/bin/python3

if __name__ == '__main__':
    import calculator_1 as calc
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print(f"{a:d} + {b:d} = {calc.sub(a, b)}")
    print("{} + {} = {}".format(a, b, calc.mul(a, b)))
    print(f"{a:d} + {b:d} = {calc.div(a, b)}")
