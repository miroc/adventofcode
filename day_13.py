#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations


def seating_value(seating, gains):
    total = 0
    for idx, name in enumerate(seating):
        left = seating[(idx-1) % len(seating)]
        right = seating[(idx+1) % len(seating)]
        total = total + gains[name][left] + gains[name][right]
    return total


def best_seating(gains):
    max_val = 0
    best = None
    for seating in permutations(gains.keys()):
        val = seating_value(seating, gains)
        if val >= max_val:
            max_val = val
            best = seating
    print(max_val, best)


def main():
    with open("day_13_input") as f:
        lines = f.readlines()
        gains = defaultdict(dict)
        for line in lines:
            x = line.strip()[:-1] # remove dot
            words = x.split()

            name, op, units, next_person = words[0], words[2], words[3], words[-1]
            gain = int(units) if op == 'gain' else -1*int(units)
            gains[name][next_person] = gain
        best_seating(gains)

        my_name = "Miro"
        existing_names = gains.keys()
        for existing_name in list(existing_names):
            gains[my_name][existing_name] = 0
            gains[existing_name][my_name] = 0
        best_seating(gains)


if __name__ == '__main__':
    main()
