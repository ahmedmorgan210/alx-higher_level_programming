#!/user/bin/python3
"""
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()

"""


def uppercase(str):
    x = ""
    for letter in str:
        if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
            x += letter
            #print(letter)
            #return
        elif ord(letter) < 65:
            x += letter
        else:
            x += chr(ord(letter) - 32)
            #x += letter
            #print(x)
            #return
    print(x)