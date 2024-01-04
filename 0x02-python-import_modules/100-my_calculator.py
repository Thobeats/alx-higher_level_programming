#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as calc
    from sys import argv, exit
    args_count = len(argv) - 1
    if args_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if operator == '+':
        print(f"{a} + {b} = {calc.add(a, b)}")
    elif operator == '-':
        print(f"{a} + {b} = {calc.sub(a, b)}")
    elif operator == '*':
        print(f"{a} + {b} = {calc.mul(a, b)}")
    elif operator == '/':
        print(f"{a} + {b} = {calc.div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
