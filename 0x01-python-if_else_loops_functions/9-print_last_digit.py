#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number) % 10
    print(num, end="")
    return num
