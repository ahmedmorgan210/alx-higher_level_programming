#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        printed_items = 0
        i = 0

        for item in my_list:
            if printed_items >= x:
                break

            print("{}".format(item), end="")
            printed_items += 1

        print()

        return printed_items

    except IndexError:
        print("Index out of range")
