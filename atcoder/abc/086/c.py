#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    txys = ((map(int, line.split())) for line in sys.stdin.readlines())

    pt, px, py = 0, 0, 0
    for t, x, y in txys:
        timeleft =  t - pt - abs(x - px) - abs(y - py)
        if timeleft < 0 or timeleft % 2 == 1:
            print('No')
            break
        pt, px, py = t, x, y
    else:
        print('Yes')


if __name__ == '__main__':
    main()
