#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    s = tuple(map(int, sys.stdin.readline().strip()))

    n = len(s)
    k = n
    for i in range(1, n):
        if s[i - 1] != s[i]:
            k = min(k, max(i, n - i))

    print(k)

if __name__ == '__main__':
    main()
