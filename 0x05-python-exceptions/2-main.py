#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

mylist = [1, 2, 3, 4]
x = len(mylist) + 4

nb_print = safe_print_list_integers(mylist, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(mylist, len(mylist))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(mylist) + 2)
print("nb_print: {:d}".format(nb_print))
