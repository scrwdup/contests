# -*- coding: utf-8 -*-

isprime = None

def sieve(n):
    global isprime

    if n < 2:
        isprime = [False] * (n + 1)
        return

    isprime = [True if i % 2 != 0 else False for i in range(n + 1)]
    isprime[0] = isprime[1] = False
    isprime[2] = True

    from math import sqrt

    for i in range(3, int(sqrt(n)) + 1):
        if isprime[i] == True:
            for j in range(i + i, n + 1, i):
                isprime[j] = False
