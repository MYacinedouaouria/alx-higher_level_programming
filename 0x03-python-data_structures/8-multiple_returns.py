#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == 0):
        r = (0, None)
    r = (len(sentence), sentence[0])
    return r
