#!/usr/bin/env python
from itertools import product

teaspoons = 100
ingredients = {"Sprinkles": {"capacity": 5, "durability": -1, "flavor": 0, "texture": 0, "calories": 5},
           "PeanutButter": {"capacity": -1, "durability": 3, "flavor": 0, "texture": 0, "calories": 1},
           "Frosting": {"capacity": 0, "durability": -1, "flavor": 4, "texture": 0, "calories": 6},
           "Sugar": {"capacity": -1, "durability": 0, "flavor": 0, "texture": 2, "calories": 8}}

# ingredients = {"Butterscotch": {"capacity": -1, "durability": -2, "flavor": 6, "texture": 3, "calories": 8},
#             "Cinnamon": {"capacity": 2, "durability": 3, "flavor": -2, "texture": -1, "calories": 3}}

names = list(ingredients.keys())


def value(combination, requested_calories=None):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    for idx, count in enumerate(combination):
        capacity += ingredients[names[idx]]["capacity"] * count
        durability += ingredients[names[idx]]["durability"] * count
        flavor += ingredients[names[idx]]["flavor"] * count
        texture += ingredients[names[idx]]["texture"] * count
        calories += ingredients[names[idx]]["calories"] * count
    total = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
    if requested_calories is not None and calories != requested_calories:
        # if not exactly as requested calories, dump the cake - 0 value
        return 0
    return total


def main():

    maximum = 0
    maximum_with_500_cals = 0
    for combination in product(range(101), repeat=4):
        if sum(combination) != 100:
            continue
        maximum = max(maximum, value(combination))
        maximum_with_500_cals = max(maximum_with_500_cals, value(combination, 500))

    print("the best cookie we can get:", maximum)
    print("the best cookie we can get with 500 calories:", maximum_with_500_cals)


if __name__ == '__main__':
    main()
