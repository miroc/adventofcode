#!/usr/bin/env python
import re
import json


def count_simple(content):
    sm = sum([int(num) for num in re.findall(r'-?\d+', content)])
    print(sm)


def pretty_print(json_data):
    print(json.dumps(json_data, sort_keys=True, indent=1, separators=(',', ': ')))


def sm(data):
    if type(data) is list:
        return sum([sm(x) for x in data])
    elif type(data) is dict:
        for a in data:
            if data[a] == 'red':
                return 0
        return sum([sm(data[a]) for a in data])
    elif type(data) is str:
        return 0
    else:
        return int(data)


def process(content):
    json_data = json.loads(content)
    print(sm(json_data))


def main():
    with open("day_12_input") as f:
        content = f.read()
        process(content)


if __name__ == '__main__':
    main()
