#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n, y = map(int, sys.stdin.readline().split())

    for i in range(y // 10000, -1, -1):
        z = y - 10000 * i
        for j in range(z // 5000, -1, -1):
            k = n - i - j
            if z == 5000 * j + 1000 * k:
                print(i, j, k)
                sys.exit()
    else:
        print('-1 -1 -1')

if __name__ == '__main__':
    main()
