#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_num = 0
    for y in my_list[:x]:
        try:
            if isinstance(y, int):
                print("{:d}".format(y), end='')
                printed_num += 1
        except TypeError:
            continue
        except IndexError:
            print("index out of range")
    print()
    return printed_num
