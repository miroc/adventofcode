#!/usr/bin/env python


def task1(lines):
    answer1 = 0
    for l in lines:
        line = l.strip()
        answer1 += len(line) - len(eval(line))
    print(answer1)


def task2(lines):
    answer2 = 0
    for l in lines:
        line = l.strip()
        answer2 += line.count('\\') + line.count('"') + 2
    print(answer2)


def main():
    lines = open("day_8_input").readlines()
    task1(lines)
    task2(lines)


if __name__ == '__main__':
    main()