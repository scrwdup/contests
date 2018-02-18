#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    c = tuple(tuple(map(int, line.split())) for line in sys.stdin.readlines())
    b = c[0]
    a = [None] * 3
    for i in range(3):
        a[i] = c[i][i] - b[i]
        for j in range(3):
            if a[i] + b[j] != c[i][j]:
                print('No')
                sys.exit()
    print('Yes')

if __name__ == '__main__':
    main()
