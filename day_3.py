#!/usr/bin/env python

def santa(inp):
    # santa coordinates
    x = 0
    y = 0
    # robo + santa coordinates
    loc = [[0, 0], [0, 0]]

    # number of visits in each location, first location gets visit by default
    visits = {(0, 0): 1}
    visits2 = {(0, 0): 1}

    for idx, c in enumerate(inp):
        loc_ind =  idx % 2


        if c == '^':
            y += 1
            loc[loc_ind][1] += 1
        elif c == '>':
            x += 1
            loc[loc_ind][0] += 1
        elif c == '<':
            x -= 1
            loc[loc_ind][0] -= 1
        else:  # c== 'v'
            y -= 1
            loc[loc_ind][1] -= 1

        key = (x,y)
        key2 = (loc[loc_ind][0], loc[loc_ind][1])

        if key in visits:
            visits[key] += 1
        else:
            visits[key] = 1

        if key2 in visits2:
            visits2[key2] += 1
        else:
            visits2[key2] = 1

    print(len(visits))
    print(len(visits2))


def main():
    with open("day_3_input") as f:
        inp = f.read()
        santa(inp)

if __name__ == '__main__':
    main()
