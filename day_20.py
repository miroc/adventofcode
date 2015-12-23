#!/usr/bin/env python
import math


def divisor_generator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


def divisors_bigger_than(num, min):
    return [x for x in divisor_generator(num) if x >= min]


def presents_count(house_num):
    p = divisor_generator(house_num)
    return sum(list(p))*10


def presents_count2(house_num):
    p = divisors_bigger_than(house_num, house_num // 50)
    return sum(list(p))*11


def task1(goal):
    for i in range(1, 1000000):
        total = presents_count(i)
        if i % 10000 == 0:
            print(i, total)
        if total >= goal:
            print("win", i)
            break


def task2(goal):
    for i in range(50000, 1000000):
        total = presents_count2(i)
        if i % 10000 == 0:
            print(i, total)
        if total >= goal:
            print("win", i)
            break


def main():
    goal = 34000000
    task1(goal)
    task2(goal)


if __name__ == '__main__':
    main()
