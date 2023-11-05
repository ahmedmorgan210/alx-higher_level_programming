#!/usr/bin/python3
"""
printing the names defined by the compiled module
that does not start with "__"

"""
if __name__ == "__main__":

    import hidden_4

    for name in dir(hidden_4):
        if "__" in name:
            continue
        print(name)
