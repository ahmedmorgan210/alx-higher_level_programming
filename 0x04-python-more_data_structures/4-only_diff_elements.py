#!/usr/bin/python3
"""function that returns a set of all elements present in only one set.\
        can be done by using (operator) set_1 ^ set_2
        OR
        by function (.symmetric_difference)
        set_1.symmetric_difference(set_2)"""


def only_diff_elements(set_1, set_2):
    return set_1.symmetric_difference(set_2)
