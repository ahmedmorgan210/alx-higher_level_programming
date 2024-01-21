#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_num = 0
    len_list = 0
    for _ in my_list:
        len_list += 1
    if x > len_list:
        raise IndexError("Index Error: x is greater than the len of list")
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
