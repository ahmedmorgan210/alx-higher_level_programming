#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv)

    if argc == 1:
        print("{} arguments.".format(0))

    elif argc == 2:
        print("{} argument:".format(argc - 1))
        print(f"{1}: {sys.argv[1]}")

    else:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print(f"{i}: {sys.argv[i]}")
