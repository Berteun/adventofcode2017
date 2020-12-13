#!/usr/bin/env python
# -*- coding: utf-8 -*-
def read_input():
    scanners = {}
    for l in open("input"):
        n, d = l.strip().split(": ")
        scanners[int(n)] = int(d)
    return scanners

def simulate(pos, scanners):
    end = max(scanners.keys()) + 1
    scanner_pos = { s : 0 for s in scanners }
    scanner_dir = { s : 1 for s in scanners }
    caught = 0
    while pos < end:    
        if pos in scanner_pos and scanner_pos[pos] == 0:
            caught += scanners[pos] * pos
        for s in scanner_pos:
            np = scanner_pos[s] + scanner_dir[s]
            if np == scanners[s]:
                scanner_dir[s] = -1
                scanner_pos[s] -= 1
            elif np == -1:
                scanner_dir[s] = 1
                scanner_pos[s] += 1
            else:
                scanner_pos[s] = np
        pos += 1
    return caught

def main():
    scanners = read_input()
    print(simulate(0, scanners))

if __name__ == '__main__':
    main()
