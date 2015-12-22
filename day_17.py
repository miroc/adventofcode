#!/usr/bin/env python


def combs(containers, liters, container_limit=None):
    if container_limit is not None and container_limit < 0:
        return 0
    if len(containers) >= 0 and liters == 0:
        return 1
    elif len(containers) == 0 or liters <= 0:
        return 0

    total = 0
    for idx, container in enumerate(containers):
        leftover = liters - container
        total += combs(containers[idx+1:], leftover, None if container_limit is None else container_limit - 1)
    return total


def smallest(sorted_containers, liters):
    for idx, container in enumerate(sorted_containers):
        leftover = liters - container
        if leftover == 0:
            return [container]
        res = smallest(sorted_containers[idx+1:], leftover)
        if res is not None:
            return [container] + res
    return None


def main():
    containers = []
    liters = 150
    with open("day_17_input") as f:
        for line in f.readlines():
            containers.append(int(line.strip()))
    print("Task1 combinations count:", combs(containers, liters))

    sorted_containers = list(reversed(sorted(containers)))
    # limit is given by the smallest possible number of containers we have to use
    container_limit = len(smallest(sorted_containers, liters))
    print("Task2 combinations count: ", combs(containers, liters, container_limit))


if __name__ == '__main__':
    main()
