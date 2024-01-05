#!/usr/bin/python3

# for letter in range(ord('z'), ord('a')-1, -1):
#     print("{}{}".format(chr(letter), chr(letter - 32)), end="")

for letter in range(ord('z'), ord('a')-1, -1):

    if letter % 2:
        new_letter = letter - 32
    else:
        new_letter = letter
    print("{}".format(chr(new_letter)), end="")
