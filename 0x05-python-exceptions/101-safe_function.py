#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = exec(fct, *args)
        return result

    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
