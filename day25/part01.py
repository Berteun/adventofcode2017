#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

def parse_begin(begin):
    a, b = begin.split("\n")
    return a[-2], int(b.split()[-2])

def parse_state(state):
    lines = state.split("\n")
    name = lines[0][-2]
    instr = {}
    instr[int(lines[1][-2])] = (int(lines[2][-2]), 1 if lines[3][-3] == "h" else -1, lines[4][-2])
    instr[int(lines[5][-2])] = (int(lines[6][-2]), 1 if lines[7][-3] == "h" else -1, lines[8][-2])
    return name, instr

def parse_states(states):
    d = {}
    for s in states:
        name, instr = parse_state(s)
        d[name] = instr
    return d

def read_input():
    f = open("input").read().strip()
    parts = f.split("\n\n")
    begin, states = parts[0], parts[1:]
    start_state, steps = parse_begin(begin)
    return start_state, steps, parse_states(states)

def simulate(start_state, steps, instr):
    tape = defaultdict(int)    
    pos = 0
    state = start_state
    for n in range(steps):
        cur_value = tape[pos]
        (outp, delta, new_state)= instr[state][cur_value]
        tape[pos] = outp
        pos += delta
        state = new_state

    return tape
        
def main():
    inp = read_input()
    start_state, steps, instr = inp
    tape = simulate(start_state, steps, instr)
    print(sum(tape.values()))
if __name__ == '__main__':
    main()
