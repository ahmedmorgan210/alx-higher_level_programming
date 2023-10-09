#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if digit > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5\n")
elif digit == 0:
    print(f"Last digit of {number} is {digit} ) and is 0\n")
elif digit < 6 and digit not 0:
    print(f"""Last digit of {number} is {digit} )
    and is less than 6 and not 0\n""")
