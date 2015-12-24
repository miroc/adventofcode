#!/usr/bin/env python
import re

from itertools import combinations


def qe(lst):
    total = 1
    for l in lst:
        total *= l
    return total


def le_fu(take_first, reversed_nums):
    biggest_nums = reversed_nums[:take_first]
    # minimal count of first group is 5
    # print(take_first, biggest_nums)
    for first_group_count in range(4, take_first):
        # print('first group count', first_group_count)
        for n in combinations(biggest_nums, first_group_count):
            # print(n)
            # if sum(n) == 507:
            #     print("task1: 507 sum found", n)
            #     return
            # elif sum(n) == 508:
            #     print("task1: 508 sum found", n)
            #     return
            if sum(n) == 380:
                print("task2: 380 sum found, QE ", n, qe(n))
                return
            elif sum(n) == 381:
                print("task1: 381 sum found", qe(n))
                return


def main():
    nums = []

    lines = open("day_24_input").read().split("\n")
    for l in lines:
        nums.append(int(l))

    print("total len=%d, sum=%d" % (len(nums), sum(nums)))

    nums.reverse()
    # not a complete solution...
    for first_group_count in range(4, 20):
        le_fu(first_group_count, list(nums))

if __name__ == '__main__':
    main()
