#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
from enum import Enum

class Instructions(Enum):
    SET = 1
    SUB = 2
    MUL = 3
    JNZ = 4

def read_input():
    instructions = []
    for l in open("input"):
        cmd, *args = l.strip().split()
        instructions.append((Instructions[cmd.upper()], [a if len(a) == 1 and a.isalpha() else int(a) for a in args]))
    return instructions

def is_reg(arg):
    return not isinstance(arg, int)

def get_value(regs, arg):
    if is_reg(arg):
        return regs[arg]
    else:
        return arg

def process(inp):
    pos = 0
    max_pos = len(inp) - 1
    regs = defaultdict(int)
    regs["a"] = 1
    muls = 0
    while 0 <= pos <= max_pos:
        print(pos, regs, inp[pos])
        instr, args = inp[pos]
        if instr == Instructions.SET:
            regs[args[0]] = get_value(regs, args[1])
            pos += 1
        elif instr == Instructions.SUB:
            regs[args[0]] -= get_value(regs, args[1])
            pos += 1
        elif instr == Instructions.MUL:
            regs[args[0]] *= get_value(regs, args[1])
            pos += 1
        elif instr == Instructions.JNZ:
            v = get_value(regs, args[0])
            if v != 0:
                pos += get_value(regs, args[1])
            else:
                pos += 1
        else:
            raise RuntimeError("Impossible " + str(instr))
    return regs[h]
def main():
    inp = read_input()
    s = process(inp)
    print(s)

if __name__ == '__main__':
    main()
