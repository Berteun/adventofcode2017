#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    return [int(b) for b in f.readline().strip().split()]

seen = set()

def redistribute(banks, idx):
    todo = banks[idx]
    banks[idx] = 0
    while todo > 0:
        idx = (idx + 1) % len(banks)
        banks[idx] += 1
        todo -= 1
    return banks

def main():
    banks = read_input()
    redistributions = 0
    while True:
        max_bank = max(banks)
        idx = banks.index(max_bank)
        banks = redistribute(banks, idx)
        redistributions += 1
        tbanks = tuple(banks) 
        if tbanks in seen:
            break
        else:
            seen.add(tbanks)
    print(redistributions)

if __name__ == '__main__':
    main()
