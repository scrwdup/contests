#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    x, y = map(int, sys.stdin.readline().split())

    cnt = 0
    i = x
    while i <= y:
        cnt += 1
        i += i

    print(cnt)

if __name__ == '__main__':
    main()
