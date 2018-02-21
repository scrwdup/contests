#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    a = map(int, sys.stdin.readline().split())

    d = {}
    for e in a:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    cnt = 0
    for k, v in d.items():
        if k < v:
            cnt += v - k
        elif k > v:
            cnt += v

    print(cnt)

if __name__ == '__main__':
    main()
