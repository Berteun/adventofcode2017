#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse_instr(instr):
    if instr[0] == 's':
        return ('spin', int(instr[1:]))
    elif instr[0] == 'x':
        to, fr = instr[1:].split("/")
        return ('exch', int(to), int(fr))
    elif instr[0] == 'p':
        to, fr = instr[1:].split("/")
        return ('part', to, fr)

def read_input():
    f = open("input")
    return [parse_instr(instr) for instr in f.readline().strip().split(",")]

def dance(lineup, inp):
    lineup = lineup[:]
    for instr in inp:
        if instr[0] == 'spin':
            x = instr[1]
            lineup = lineup[-x:] + lineup[:-x]
        elif instr[0] == 'exch':
            t,f = instr[1], instr[2]
            lineup[t],lineup[f] = lineup[f],lineup[t]
        elif instr[0] == 'part':
            t,f = instr[1], instr[2]
            ti = lineup.index(t)
            fi = lineup.index(f)
            lineup[ti],lineup[fi] = lineup[fi],lineup[ti]
        else:
            raise RuntimeError("not possible")

    return lineup

def find_cycle_length(start, inp):
   result = start[:]
   n = 0
   while True:
       result = dance(result[:], inp)
       n += 1
       if result == start:
           return n

def main():
   inp = read_input() 
   start = [chr(ord('a') + n) for n in range(16)]
   result = dance(start, inp) 

   cycle_length = find_cycle_length(start, inp)

   result = start[:]
   for n in range(1000000000 % cycle_length):
       result = dance(result[:], inp) 
   print(''.join(result))

if __name__ == '__main__':
    main()
