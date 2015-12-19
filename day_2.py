#!/usr/bin/env python

def main():
    fname = 'day_2_input'
    square_feet_total = 0
    ribbon_feet = 0

    with open(fname) as f:
        content = f.readlines()
        for line in content:
            # read dimensions [l, w, h], and convert to ints
            # dimens = map(int, line.strip().split('x'))
            dimens = [int(s) for s in line.strip().split('x')]
            [a, b, c] = sorted(dimens)
            # take smallest side 3 times - extra paper
            square_feet_total += 3*a*b + 2*b*c + 2*c*a

            # elves' equation for ribbon length
            ribbon_feet += 2*a + 2*b + a*b*c

    print("total square feet %d" % square_feet_total)
    print("ribbon feet length %d" % ribbon_feet)

if __name__ == '__main__':
    main()
