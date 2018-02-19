#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

isprime = None

def sieve(n):
    global isprime

    if n < 2:
        isprime = [False] * (n + 1)
        return

    isprime = [True if i % 2 != 0 else False for i in range(n + 1)]
    isprime[0] = isprime[1] = False
    isprime[2] = True

    from math import sqrt, ceil

    for i in range(3, int(sqrt(n)) + 1):
        if isprime[i] == True:
            for j in range(i + i, n + 1, i):
                isprime[j] = False

def main():
    global isprime

    sieve(100000)

    _ = sys.stdin.readline()

    csums = [0] * 100001
    for i in range(3, 100001):
        csums[i] += csums[i - 1]
        if isprime[i] == True and isprime[(i + 1) // 2] == True:
            csums[i] += 1

    for l, r in (map(int, line.split()) for line in sys.stdin.readlines()):
        print(csums[r] - csums[l - 1])

if __name__ == '__main__':
    main()
