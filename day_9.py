#!/usr/bin/env python
import re


class Computer:
    def __init__(self):
        self.registry = {}
        self.computed = {}

    def add(self, target, to_eval):
        self.registry[target] = to_eval

    def eval(self, target):
        if target in self.computed:
            return self.computed[target]

        if target.isdigit():
            return int(target)

        val = self.registry[target]

        f = val["func"]
        p = val["params"]
        if f == "LSHIFT":
            res = self.eval(p[0]) << self.eval(p[1])
        elif f == "RSHIFT":
            res = self.eval(p[0]) >> self.eval(p[1])
        elif f == "AND":
            res = self.eval(p[0]) & self.eval(p[1])
        elif f == "OR":
            res = self.eval(p[0]) | self.eval(p[1])
        elif f == "NOT":
            res = ~self.eval(p[0])
        else:
            res = self.eval(p[0])

        # Store computed value for particular symbol
        self.computed[target] = res
        return res


computer = Computer()

# (\w) matches [a-zA-Z0-9_]
assign_regex = re.compile("(.+) -> (\w+)")

targets = []


def process_line(line):
    # print(line)
    m = assign_regex.match(line)
    if m is not None:
        target = m.group(2)
        targets.append(target)
        left_side = m.group(1).split()

        twoparams_func = ["RSHIFT", "LSHIFT", "OR", "AND"]
        for f in twoparams_func:
            if f in left_side:
                computer.add(target, {"func": f, "params": [left_side[0], left_side[2]]})
                return

        # one parameter funcs - NOT and ASSIGN
        if "NOT" in left_side:
            computer.add(target, {"func": "NOT", "params": [left_side[1]]})
        else:
            computer.add(target, {"func": None, "params": [left_side[0]]})


def process_lines(lines):
    for line in lines:
        process_line(line)


def main():
    with open("day_7_input") as f:
        lines = f.readlines()
        process_lines(lines)

        a = computer.eval("a")

        print("'a' evaluates to %d" % a)
        computer.computed = {"b": a}

        a2 = computer.eval("a")

        print("'a2' evaluates to %d" % a2)


if __name__ == '__main__':
    main()
