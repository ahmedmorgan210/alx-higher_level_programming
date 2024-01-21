#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    printed_num = 0
    for i in range(x):
        try:
            y = my_list[i]
            if isinstance(y, int):
                print("{:d}".format(y), end='')
                printed_num += 1
        except TypeError:
            continue
        except IndexError:
            raise IndexError("List index out of range")
    print()
    return printed_num
