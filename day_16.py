#!/usr/bin/env python

tape_data = {"children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1}

sues = {}


def main():
    for line in open("day_16_input").readlines():
        _, name, p1, v1, p2, v2, p3, v3 = line.strip().split()
        sues[int(name[:-1])] = {p1[:-1]: int(v1[:-1]), p2[:-1]: int(v2[:-1]), p3[:-1]: int(v3)}

    for sue_num in sues:
        if all([attr_name in tape_data and tape_data[attr_name] == sues[sue_num][attr_name] for attr_name in sues[sue_num]]):
            print("task1 sue num:", sue_num)
            break

    for sue_num in sues:
        restart = False
        for attr_name in sues[sue_num]:
            if attr_name not in tape_data:
                continue
            if attr_name in ("cats", "trees"):
                if sues[sue_num][attr_name] <= tape_data[attr_name]:
                    restart = True
                    break
            elif attr_name in ("pomeranians", "goldfish"):
                if sues[sue_num][attr_name] >= tape_data[attr_name]:
                    restart = True
                    break
            else:
                if tape_data[attr_name] != sues[sue_num][attr_name]:
                    restart = True
                    break
        if restart:
            continue
        print("task2 sue num:", sue_num)
        return


if __name__ == '__main__':
    main()
