#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    s, t = (line.strip() for line in sys.stdin.readlines())
    if sorted(s) < sorted(t, reverse=True):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
