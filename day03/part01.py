#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    #print(inp, "sits in square {0}x{0} on position {1}".format(square_size, pos_in_square))

    quadrant = pos_in_square // (quadrant_size)
    pos_in_quadrant = pos_in_square % quadrant_size

    #print(inp, "sits in quadrant {}, on position {}".format(quadrant, pos_in_quadrant))

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

def main():
    inp = read_input()
    x, y = get_coordinates(inp)
    print(abs(x) + abs(y))

if __name__ == '__main__':
    main()
