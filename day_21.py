#!/usr/bin/env python

from itertools import combinations
from itertools import product
import sys

boss_hit_points= 103
boss_damage = 9
boss_armor = 2

weapons_input= """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

armor_input="""Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""

rings_input="""Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3"""


class Item:
    def __init__(self, name, cost, damage, armor):
        self.name= name
        self.cost = int(cost)
        self.damage = int(damage)
        self.armor = int(armor)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{%s, cost=%d, damage=%d, armor=%d}" % (self.name, self.cost, self.damage, self.armor)


def parse(inp):
    items = []
    for line in inp.split("\n"):
        name, cost, damage, armor = line.strip().split()
        items.append(Item(name, cost, damage, armor))
    return items


def check_win(stats):
    my_cost = 0
    my_damage = 0
    my_armor = 0
    my_hit_points = 100

    opponent_hit_points = boss_hit_points

    for p in stats:
        for item in p:
            my_cost += item.cost
            my_damage += item.damage
            my_armor += item.armor

    # Let's kill each other
    while True:
        # my hit
        opponent_hit_points = hit(opponent_hit_points, boss_armor, my_damage)
        if opponent_hit_points <= 0:
            return True, my_cost

        # opponent hit
        my_hit_points = hit(my_hit_points, my_armor, boss_damage)
        if my_hit_points <= 0:
            return False, my_cost


def hit(defender_health, defender_armor, attacker_damage):
    return defender_health - max(1, attacker_damage-defender_armor)


def main():
    none_item = Item("none", 0, 0, 0)
    weapons = parse(weapons_input)
    # we can select 0-1 armors, therefore add one none-item
    armors = parse(armor_input)
    armors.append(none_item)
    # we can select 0-2 rings, therefore add two none-items
    rings = parse(rings_input)
    rings.append(none_item)
    rings.append(none_item)
    # print(weapons[0], armors[0], rings[0])

    min_win_cost = sys.maxsize
    max_lose_cost = 0

    for stats in list(product(combinations(weapons, 1), combinations(armors, 1), combinations(rings, 2))):
        is_winning, cost = check_win(stats)
        if is_winning:
            min_win_cost = min(min_win_cost, cost)
        else:
            max_lose_cost = max(max_lose_cost, cost)

    print("Minimal win cost = %d, maximal lose cost = %d" % (min_win_cost, max_lose_cost))

if __name__ == '__main__':
    main()
