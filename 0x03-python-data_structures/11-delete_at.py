#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    # if len(my_list) == 0:
    #     return None

    new_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return my_list
    elif idx >= 0 and len(my_list) != 0:
        del new_list[idx]
        return new_list
