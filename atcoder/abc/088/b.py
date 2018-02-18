#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    a = sorted(map(int, sys.stdin.readline().split()), reverse=True)
    s = [[], []]
    for i, b in enumerate(a):
        s[i % 2].append(b)
    print(sum(s[0]) - sum(s[1]))

if __name__ == '__main__':
    main()
