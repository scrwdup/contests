#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()

    for i, c in enumerate(s):
        if i != a:
            if c.isdigit() == True and 0 <= int(c) <= 9:
                continue
        elif c == '-':
            continue
        break
    else:
        print('Yes')
        sys.exit()

    print('No')

if __name__ == '__main__':
    main()
