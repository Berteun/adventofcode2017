#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    return [l.strip("\n") for l in open("input")]

def find_start(maze):
    return 0, maze[0].index("|")

def next_coordinate(x, y, d):
    if d == 'D':
        return (x, y + 1)
    if d == 'U':
        return (x, y - 1)
    if d == 'L':
        return (x - 1, y)
    if d == 'R':
        return (x + 1, y)

def print_maze(maze, y, x):
    pmaze = [list(r[:]) for r in maze]
    pmaze[y][x] = 'X'
    print("\n".join(''.join(r) for r in pmaze))
    print()

def main():
    maze = read_input()
    maxx = len(maze[0])
    maxy = len(maze)

    y, x = find_start(maze)
    d = 'D'
    letters = []
    steps = 0
    while maze[y][x] != ' ':
        #print_maze(maze, y, x)
        x, y = next_coordinate(x, y, d)
        steps += 1
        if maze[y][x] == '+':
            if d in ['U', 'D']:
                test = ['L', 'R']
            else:
                test = ['U', 'D']
            for d in test:                    
                nx, ny = next_coordinate(x, y, d)
                if nx >= 0 and ny >= 0 and nx < maxx and ny < maxy and maze[ny][nx] not in [' ']:
                    break
            else:
                raise RuntimeError("Cannot determine new direction", x, y)
        elif maze[y][x].isalpha():
            letters.append(maze[y][x])

    print(''.join(letters), steps)

if __name__ == '__main__':
    main()
