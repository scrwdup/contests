#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = int(input())
    if (n % 500) > a:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()
