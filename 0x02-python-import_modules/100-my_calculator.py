#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    num = len(argv)
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if operator == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif operator == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif operator == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
