#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    results = {}
    weights = {}
    for l in f:
        if "->" in l:        
            left, right = l.split("->")
        else:
            left, right = l, ""
        
        source, weight = left.strip().split(' ', 2)
        weight = int(weight.strip()[1:-1])
        weights[source] = weight
        if right:
            targets = right.strip().split(", ")
        else:
            targets = []
        results[source] = targets
    return results, weights

def find_bottom(inp):
    all_sources = set()
    all_targets = set()
    for (source, targets) in inp.items():
        all_sources.add(source)
        all_targets.update(set(targets))
    return (all_sources - all_targets).pop()

def compute_weight(bottom, results, weights):
    weight = weights[bottom]
    queue = results[bottom][:]
    while queue:
        nxt = queue.pop(0)
        weight += weights[nxt]
        queue.extend(results[nxt])
    return weight

def find_unbalance(bottom, parent, results, weights):
    current = bottom
    children = results[bottom]
    ws = [compute_weight(child, results, weights) for child in children]
    unb = False
    if not all(w == ws[0] for w in ws):
        unb = True
        mx = max(ws)
        idx = ws.index(mx)
        node = children[idx]
        d = max(ws) - min(ws)
        #print('>>>',bottom, children, ws, max(ws) - min(ws), weights[node] - d)
        if not any(find_unbalance(c, current, results, weights) for c in children):
            print(weights[node] - d)
    return unb 

def main():
    results, weights = read_input()
    bottom = find_bottom(results)
    find_unbalance(bottom, None, results, weights)

if __name__ == '__main__':
    main()

