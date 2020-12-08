#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    results = []
    for l in f:
        if "->" in l:        
            left, right = l.split("->")
        else:
            left, right = l, ""
        
        source = left.split(' ', 1)[0]
        if right:
            targets = right.strip().split(", ")
        else:
            targets = []
        results.append((source, targets))
    return results

def find_bottom(inp):
    all_sources = set()
    all_targets = set()
    for (source, targets) in inp:
        all_sources.add(source)
        all_targets.update(set(targets))
    return all_sources - all_targets

def main():
    inp = read_input()
    print(find_bottom(inp).pop())

if __name__ == '__main__':
    main()

