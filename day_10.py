#!/usr/bin/env python
from itertools import takewhile
from itertools import groupby

def say(text):
    rest = text
    result = ""
    while len(rest) > 0:
        prefix, rest = prefix_and_rest(rest)
        result += say_part(prefix)
    return result


def say_part(text_all_same):
    return str(len(text_all_same)) + text_all_same[0]


def prefix_and_rest(text):
    c = text[0]
    prefix = list(takewhile(lambda x: x == c, iter(text)))
    return prefix, text[len(prefix):]


def recal(challenge):
    pass


def main():
    challenge = "1321131112"
    # for key, grouper in groupby(challenge):
    #     print(key, len(list(grouper)))

    a = challenge
    for i in range(50):
        print(i)
        a = say(a)
    print(len(a))

if __name__ == '__main__':
    main()
