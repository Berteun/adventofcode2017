#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_start_grid():
    return [['.#.','..#','###']]

def read_input():
    rules = []
    for l in open('input'):
        l = l.strip()
        fr, to = l.split(' => ')
        rules.append((fr.split('/'), to.split('/')))
    return rules

def flip(g):
    return g[::-1]

def rotate(g):
    return list(''.join(l) for l in zip(*g[::-1]))

def rule_applies(g, r):
    for _ in range(2):
        for _ in range(4):
            #print("testing", g, "and", r)
            if g == r[0]:
                return True
            g = rotate(g)
        g = flip(g)
    return False

def apply_rule(g, r):
    return r[1][:]

def apply_rules(rules, grid):
    new_grid = []
    for row in grid:
        new_grid.append([])
        for tile in row:
            for r in rules:
                if rule_applies(tile, r):
                    new_grid[-1].append(apply_rule(tile, r))
                    continue
    return new_grid

def join_grid(g):
    joined = []
    for row in g:
        for n in range(len(row[0])):
            joined.append("".join(t[n] for t in row))
    return(joined)

def extract_tile(grid, size, y, x):
    #print(grid, size, y, x)
    tile = [grid[(y*size) + n][(x*size):(x+1)*size] for n in range(size)]
    #print(grid, size, y, x, tile)
    return tile

def split_grid(grid):
    #print("g", grid)
    full_grid = join_grid(grid)
    #print("j", full_grid)
    step_size = 3 if len(full_grid[0]) % 2 else 2
    new_grid = []
    for y in range(len(full_grid)//step_size):
        new_grid.append([])
        for x in range(len(full_grid)//step_size):
            new_grid[-1].append(extract_tile(full_grid, step_size, y, x))
    return new_grid

def print_grid(grid):
    #print("g", grid)
    joined = join_grid(grid)
    #print("j", joined)
    d = int((len(joined[0]) * len(joined))**(.5))
    #print("d", d)
    row_size = len(joined) // d
    for n in range(d):
       print("|".join(joined[row_size*n:row_size*(n+1)]))

def count_on(grid):
    return "".join(join_grid(grid)).count('#')

def main():
    rules = read_input()

    #print(rules)
    grid = get_start_grid()
    #print(grid)

    for n in range(5):
        #print_grid(grid)
        #print("")
        #print('splitting', grid)
        grid = split_grid(grid)
        #print('applying', grid)
        grid = apply_rules(rules, grid)
    #print_grid(grid)
    print(count_on(grid))

if __name__ == '__main__':
    main()
