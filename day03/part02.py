#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

def read_input():
    f = open("input")
    return int(f.readline().strip())

def get_coordinates(inp):
    if inp == 1:
        return (0, 0)

    square_size = 1
    while square_size**2 < inp:
        square_size += 2

    prev_square = square_size - 2
    quadrant_size = square_size - 1
    pos_in_square = (inp - (prev_square**2)) % (4 * quadrant_size)

    quadrant = pos_in_square // (quadrant_size)
    pos_in_quadrant = pos_in_square % quadrant_size

    square_no = square_size // 2
    if quadrant == 0:
        return (square_no, -square_no + pos_in_quadrant)
    elif quadrant == 1:
        return (square_no - pos_in_quadrant, square_no)
    elif quadrant == 2:
        return (-square_no, square_no - pos_in_quadrant)
    elif quadrant == 3:
        return (-square_no + pos_in_quadrant, -square_no)
    raise Exception("This should not happen: {}".format(inp))

cache = {(0, 0) : 1}
def get_neighbour_sum(x, y):
    s = 0
    for xd in [-1, 0, 1]: 
        for yd in [-1, 0, 1]:
            s += cache.get((x + xd, y + yd), 0)
    return s

def get_value(n):
    x, y = get_coordinates(n)
    result = get_neighbour_sum(x,y)
    cache[(x,y)] = result
    return result

def main():
    inp = read_input()
    for n in itertools.count(1):
        v = get_value(n)
        if v > inp:
            break

    print(v)

if __name__ == '__main__':
    main()
