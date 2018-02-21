#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
    a, b, c, d = map(int, input().split())
    left = a + b
    right = c + d
    if left > right:
        print('Left')
    elif left < right:
        print('Right')
    else:
        print('Balanced')

if __name__ == '__main__':
    main()
