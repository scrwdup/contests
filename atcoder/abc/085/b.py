#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    _ = sys.stdin.readline()
    print(len(set(map(int, sys.stdin.readlines()))))

if __name__ == '__main__':
    main()
