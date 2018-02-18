#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from collections import deque

def main():
    h, w = map(int, sys.stdin.readline().split())
    s = tuple(tuple(e for e in line.strip()) for line in sys.stdin.readlines())
    nwhites = sum(si.count('.') for si in s)

    que = deque([(0, 0, 1)])
    d = (1, 0, -1)
    visited = [[False] * w for _ in range(h)]
    h -= 1
    w -= 1
    while len(que) > 0:
        y, x, nsteps = que.popleft()
        if y < 0 or y > h or x < 0 or x > w or visited[y][x] == True or s[y][x] == '#':
            continue
        elif y == h and x == w:
            print(nwhites - nsteps)
            break
        visited[y][x] = True
        nsteps += 1
        que.extend([(y + dy, x + dx, nsteps) for dy in d for dx in d
                    if (dy != 0 or dx != 0) and dy * dx == 0])
    else:
        print('-1')

if __name__ == '__main__':
    main()
