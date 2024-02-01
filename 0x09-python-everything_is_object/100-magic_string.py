#!/usr/bin/python3
def magic_string(call=iter([0])):
    magic_string.call = getattr(magic_string, 'call', 0) + 1
    return ', '.join(['BestSchool'] * magic_string.call)
