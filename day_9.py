#!/usr/bin/env python
from collections import defaultdict
import itertools

# For automatic creation of nested dictionaries when assigning a value
distances = defaultdict(dict)
cities = set()

# Old way
def travel(seen_cities, total):
    last_city = seen_cities[-1]
    new_cities = [new_city for new_city in cities if new_city in distances[last_city] and new_city not in seen_cities]
    if len(new_cities) == 0:
        if len(seen_cities) == len(cities):
            # if all seen, go back
            return seen_cities, total
        else:
            # no path here
            return None

    travels = []
    for new_city in new_cities:
        newlist = list(seen_cities)
        newlist.append(new_city)
        dist = distances[last_city][new_city]
        res = travel(newlist, total + dist)
        if res is not None:
            travels.append(res)

    if len(travels) == 0:
        return None
    # First task
    return min(travels, key=lambda x: x[1])
    # Second task
    # return max(travels, key=lambda x: x[1])


def process_line(line):
    (frm, _, to, _, dist) = line.split()
    # without defaultdict, this  would throw an error
    distances[frm][to] = int(dist)
    distances[to][frm] = int(dist)
    cities.add(frm)
    cities.add(to)


def process_lines(lines):
    for line in lines:
        process_line(line)

    # New approach using permutations and zip
    path_sums = []
    for path in itertools.permutations(cities):
        total = sum([distances[frm][to] for frm,to in zip(path[:-1], path[1:])])
        path_sums.append(total)

    print("Task1: min travel distance is %d" % min(path_sums))
    print("Task2: max travel distance is %d" % max(path_sums))


def main():
    with open("day_9_input") as f:
        lines = f.readlines()
        process_lines(lines)


if __name__ == '__main__':
    main()
