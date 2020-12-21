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

def step(inp, regs, recvq, sendq, pos):
    if pos < 0 or pos >= len(inp):
        return "TERM"
    instr, args = inp[pos]
    if instr == Instructions.SND:
        v = get_value(regs, args[0])
        sendq.append(v)
        return pos + 1
    elif instr == Instructions.SET:
        regs[args[0]] = get_value(regs, args[1])
        return pos + 1
    elif instr == Instructions.ADD:
        regs[args[0]] += get_value(regs, args[1])
        return pos + 1
    elif instr == Instructions.MUL:
        regs[args[0]] *= get_value(regs, args[1])
        return pos + 1
    elif instr == Instructions.MOD:
        regs[args[0]] %= get_value(regs, args[1])
        return pos + 1
    elif instr == Instructions.RCV:
        if len(recvq) > 0:
            v = recvq.pop(0)
            regs[args[0]] = v
            return pos + 1
        else:
            return "BLCK"
    elif instr == Instructions.JGZ:
        v = get_value(regs, args[0])
        if v > 0:
            return pos + get_value(regs, args[1])
        else:
            return pos + 1
    else:
        raise RuntimeError("Impossible " + str(instr))

def process(inp):
    posA, posB = 0, 0
    regsA, regsB = defaultdict(int), defaultdict(int)
    regsA["p"], regsB["p"] = 0, 1
    bcount = 0 
    sendA = []
    sendB = []
    while True:
        newStateA = step(inp, regsA, sendB, sendA, posA)
        lb = len(sendB)
        newStateB = step(inp, regsB, sendA, sendB, posB)
        la = len(sendB)
        if la != lb:
            bcount += 1

        if newStateA in ["BLCK","TERM"] and newStateB in ["BLCK", "TERM"]:
            return bcount

        if isinstance(newStateA, int):
            posA = newStateA
        if isinstance(newStateB, int):
            posB = newStateB
    
def main():
    inp = read_input()
    s = process(inp)
    print(s)

if __name__ == '__main__':
    main()
