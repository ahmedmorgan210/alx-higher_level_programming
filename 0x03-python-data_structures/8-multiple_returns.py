#!/usr/bin/python3


def multiple_returns(sentence):
    sen_len = len(sentence)
    if sentence is None:
        return None
    #if sen_len == 0 and sentence[0] is None:
        sentence[0] = None

    return (len(sentence), sentence[0])
