#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    if a % 2 == 0 or b % 2 == 0:
        print('Even')
    else:
        print('Odd')

if __name__ == '__main__':
    main()
