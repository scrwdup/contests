#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from math import ceil

def main():
    n, h = map(int, sys.stdin.readline().split())
    k = tuple(tuple(map(int, line.split())) for line in sys.stdin.readlines())

    max_a = max(x[0] for x in k)
    b = tuple(sorted((x[1] for x in k if x[1] > max_a), reverse=True))

    cnt = 0
    for bi in b:
        h -= bi
        cnt += 1
        if h <= 0:
            break
    else:
        cnt += ceil(h / max_a)

    print(cnt)

if __name__ == '__main__':
    main()
