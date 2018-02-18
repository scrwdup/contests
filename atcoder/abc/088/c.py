#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    c = tuple(tuple(map(int, line.split())) for line in sys.stdin.readlines())
    csum = sum((sum(ci) for ci in c))
    trace = sum((c[i][i] for i in range(len(c))))
    if csum == 3 * trace:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()
