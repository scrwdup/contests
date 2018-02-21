#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from itertools import islice

def reachable(steps, x):
    m = len(steps)
    if m == 0:
        return x == 0
    n = sum(steps) + 1
    if n <= x:
        return False
    dp = [[False] * n for _ in range(m)]
    dp[0][steps[0]] = True
    for i, step in enumerate(islice(steps, 1, None)):
        for j in range(n):
            if dp[i][j] == True:
                dp[i + 1][j + step] = True
                if j - step >= 0:
                    dp[i + 1][j - step] = True
    return dp[-1][x]


def main():
    s = sys.stdin.readline().strip()
    x, y = map(int, sys.stdin.readline().split())

    i = s.find('T')
    if i != -1:
        x -= i
        i += 1
    else:
        i = len(s)
        x -= i

    xsteps = []
    ysteps = []
    cnt = 0
    nturns = 0
    for c in islice(s + 'T', i, None):
        if c == 'F':
            cnt += 1
            continue
        if cnt > 0:
            if nturns % 2 != 0:
                xsteps.append(cnt)
            else:
                ysteps.append(cnt)
            cnt = 0
        nturns += 1

    if reachable(xsteps, abs(x)) == True and reachable(ysteps, abs(y)) == True:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
