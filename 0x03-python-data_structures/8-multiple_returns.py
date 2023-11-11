#!/usr/bin/python3

def multiple_returns(sentence):
    sen_len = len(sentence)

    if sen_len == 0:
        sentence[0] = None

    return (len(sentence), sentence[0])
