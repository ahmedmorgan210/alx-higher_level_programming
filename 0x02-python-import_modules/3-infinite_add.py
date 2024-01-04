#!/usr/bin/python3
"""
creating a program to print the sum
of all argment values
"""
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)

    total = 0
"""
a loop to iterate on every single argv
adding it to the total

"""
for i in range(1, argc):
    total += int(sys.argv[i])

print(total)
