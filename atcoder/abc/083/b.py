#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n, a, b = map(int, sys.stdin.readline().split())

    s = 0
    for i in range(1, n + 1):
        if a <= sum(map(int, str(i))) <= b:
            s += i

    print(s)

if __name__ == '__main__':
    main()
