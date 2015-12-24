#!/usr/bin/env python
import re


class Inst:
    def __init__(self, args):
        pat = re.compile(r'^[-+]?\d+$')

        for idx, arg in enumerate(args):
            if arg[-1] == ',':
                    arg = arg[:-1]
            if pat.search(arg):
                if arg[0] == '-':
                    arg = -1 * int(arg[1:])
                else:
                    arg = int(arg[1:])

            if idx == 0:
                self.name = arg
            elif idx == 1:
                self.par1 = arg
            else:
                self.par2 = arg


def execute(program):
    regs = {"a": 1, "b": 0}
    index = 0
    while index in range(len(program)):
        inst = program[index]
        di = 1

        if inst.name == 'hlf':
            regs[inst.par1] //= 2
        elif inst.name == 'tpl':
            regs[inst.par1] *= 3
        elif inst.name == 'inc':
            regs[inst.par1] += 1
        elif inst.name == 'jmp':
            di = inst.par1
        elif inst.name == 'jie':
            if regs[inst.par1] % 2 == 0:
                di = inst.par2
        elif inst.name == 'jio':
            if regs[inst.par1] == 1:
                di = inst.par2
        index += di

    print(regs)


def main():
    program = []
    with open("day_23_input") as f:
        lines = f.readlines()
        for line in lines:
            pars = line.strip().split()
            program.append(Inst(list(pars)))
    execute(program)


if __name__ == '__main__':
    main()
