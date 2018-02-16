#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    lrds = ((map(int, line.split())) for line in sys.stdin.readlines())

    g = tuple([] for _ in range(n))
    x = [None] * n

    for l, r, d in lrds:
        l -= 1
        r -= 1
        g[l].append((r, d))
        g[r].append((l, -d))

    for i in range(n):
        if x[i] is not None:
            continue
        stack = [i]
        x[i] = 0
        while len(stack):
            v = stack.pop()
            for u, d in g[v]:
                if x[u] is None:
                    stack.append(u)
                    x[u] = x[v] + d

    for v in range(n):
        for u, d in g[v]:
            if x[v] + d != x[u]:
                print('No')
                sys.exit()

    print('Yes')

if __name__ == '__main__':
    main()
