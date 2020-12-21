#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
from enum import Enum

class Instructions(Enum):
    SND = 1
    SET = 2
    ADD = 3
    MUL = 4
    MOD = 5
    RCV = 6
    JGZ = 7

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
    last_sound = None
    while 0 <= pos <= max_pos:
        instr, args = inp[pos]
        if instr == Instructions.SND:
            last_sound = get_value(regs, args[0])
            print("Playing ", last_sound)
            pos += 1
        elif instr == Instructions.SET:
            regs[args[0]] = get_value(regs, args[1])
            pos += 1
        elif instr == Instructions.ADD:
            regs[args[0]] += get_value(regs, args[1])
            pos += 1
        elif instr == Instructions.MUL:
            regs[args[0]] *= get_value(regs, args[1])
            pos += 1
        elif instr == Instructions.MOD:
            regs[args[0]] %= get_value(regs, args[1])
            pos += 1
        elif instr == Instructions.RCV:
            v = get_value(regs, args[0])
            if (v != 0):
                return last_sound
            pos += 1
        elif instr == Instructions.JGZ:
            v = get_value(regs, args[0])
            if v > 0:
                pos += get_value(regs, args[1])
            else:
                pos += 1
        else:
            raise RuntimeError("Impossible " + str(instr))
def main():
    inp = read_input()
    s = process(inp)
    print(s)

if __name__ == '__main__':
    main()
