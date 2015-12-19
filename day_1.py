#!/usr/bin/env python

def found_floor(input):
    floor = 0
    first_neg_found = False
    for idx, c in enumerate(input, start=1):
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0 and not first_neg_found:
            first_neg_found = True
            print("first negative index %d (starting from one)" % idx)

    print("final floor is %d" % floor)


def main():
    f = open('day_1_input')
    inp = f.read()
    found_floor(inp)
    f.close()

if __name__ == '__main__':
    main()
