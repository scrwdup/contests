#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    csf = tuple(tuple(map(int, line.split())) for line in sys.stdin.readlines())

    ans = []
    for i in range(n - 1):
        t = 0
        for c, s, f in csf[i:]:
            if t < s:
                t = s
            k, r = divmod(t - s, f)
            if r != 0:
                t = s + (k + 1) * f
            t += c
        ans.append(t)
    ans.append(0)

    print(*ans, sep='\n')

if __name__ == '__main__':
    main()
