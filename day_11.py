#!/usr/bin/env python
import string
import re

# small english alphabet minus [i, o,   l]
# ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = string.ascii_lowercase


# decoding and encoding from universal radix taken from:
# https://stackoverflow.com/questions/1119722/base-62-conversion-in-python
def base_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X
    :param num:
    :param alphabet:
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num //= base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number
        :param string:
        :param alphabet:
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


def check_pairs(word):
    return len(re.findall(r'([a-z])\1', word)) >= 2


def check_straight(word):
    for i in range(len(word) - 2):
        if ord(word[i]) + 2 == ord(word[i + 1]) + 1 == ord(word[i + 2]):
            return True
    return False


def check_has_forbidden_letters(word, letters_re=re.compile(r'[iol]+')):
    return bool(letters_re.search(word))


def prnt(text, iters=10):
    val = base_decode(text)
    for i in range(iters):
        print(i, base_encode(val))
        val += 1

def get_next_pass(password):
    val = base_decode(password)
    while True:
        val += 1
        word = base_encode(val)
        if not check_has_forbidden_letters(word) and check_pairs(word) and check_straight(word):
            return word



def main():
    text = "cqjxjnds"

    first = get_next_pass(text)
    print(first)

    second = get_next_pass(first)
    print(second)


if __name__ == '__main__':
    main()
