#!/usr/bin/python3


def multiple_returns(sentence):
    sen_len = len(sentence)
    if sen_len == 0:
        #sentence[0] = None
        return (sen_len, None)
    #if sen_len == 0 and sentence[0] is None:
        #sentence[0] = None

    return (sen_len, sentence[0])
