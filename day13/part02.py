#!/usr/bin/env python
# -*- coding: utf-8 -*-
def read_input():
    scanners = {}
    for l in open("input"):
        n, d = l.strip().split(": ")
        scanners[int(n)] = int(d)
    return scanners


def simulate(start_pos, scanners):
    for s in scanners:
        scanner_pos = (s - start_pos) % (2*scanners[s] - 2)
        if scanner_pos == 0:
            return True
    return False

def main():
    scanners = read_input()
    delay = 1
    caught = True
    while caught:
        delay -= 1
        caught = simulate(delay, scanners)
    print(-delay)

if __name__ == '__main__':
    main()
