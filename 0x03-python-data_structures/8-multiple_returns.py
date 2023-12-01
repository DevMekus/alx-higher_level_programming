#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sen_lent = len(sentence)
    else:
        sen_lent = 0
    return (sen_lent, sentence if not sentence else sentence[:1])
