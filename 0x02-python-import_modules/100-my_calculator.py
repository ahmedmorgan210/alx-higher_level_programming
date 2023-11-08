#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    from calculator_1 import add, sub, mul, div

    argc = len(sys.argv)
    result = 0

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if sys.argv[2] == '+':
        result = add(int(sys.argv[1]), int(sys.argv[3]))
        print(f"{sys.argv[1]} + {sys.argv[3]} = {result}")
        exit(0)

    elif sys.argv[2] == '-':
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
        print(f"{sys.argv[1]} - {sys.argv[3]} = {result}")
        exit(0)

    elif sys.argv[2] == '*':
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
        print(f"{sys.argv[1]} * {sys.argv[3]} = {result}")
        exit(0)

    elif sys.argv[2] == '/':
        result = div(int(sys.argv[1]), int(sys.argv[3]))
        print(f"{sys.argv[1]} / {sys.argv[3]} = {result}")
        exit(0)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
