#!/usr/bin/python3
def uppercase(str):
    x = ""
    for letter in str:
        if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
            x += letter
        elif ord(letter) < 65:
            x += letter
        else:
            x += chr(ord(letter) - 32)
    print(x.format())
